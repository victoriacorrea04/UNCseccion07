"""BACKEND: API REST hecha con Flask + MySQL.

No devuelve paginas web, solo datos en formato JSON.
Se ejecuta en el puerto 5001:  python app.py
"""
import time

from flask import Flask, request, jsonify, abort
from pymysql.err import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from db import query
from emotion import detectar_emocion

app = Flask(__name__)

# ---------------------------------------------------------------
# Configuracion
# ---------------------------------------------------------------
PELICULAS_POR_PAGINA = 12   # cuantas peliculas devolver si no se indica "limit"
LIMITE_MAXIMO = 50          # nadie puede pedir mas de 50 de golpe

MAX_PETICIONES = 200        # peticiones permitidas por IP...
VENTANA_SEGUNDOS = 60       # ...cada 60 segundos

DIAS_SEMANA = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]

# Esta subconsulta devuelve los generos de una pelicula en un solo texto,
# por ejemplo "Drama, Romance". La usamos dentro de varias consultas.
# (JOIN entre movie_genres y genres)
GENEROS_DE_LA_PELICULA = """(
    SELECT GROUP_CONCAT(g.name SEPARATOR ', ')
    FROM movie_genres mg
    JOIN genres g ON g.id = mg.genre_id
    WHERE mg.movie_id = m.id
)"""


# ---------------------------------------------------------------
# Limite de peticiones (rate limit)
# ---------------------------------------------------------------
visitas = {}   # guarda, para cada IP, la hora de sus ultimas peticiones


@app.before_request
def limitar_peticiones():
    """Se ejecuta antes de cada peticion. Si una IP pide demasiado, responde 429."""
    if not request.path.startswith("/api"):
        return  # solo limitamos la API, no las imagenes

    ahora = time.time()
    ip = request.remote_addr

    # Nos quedamos solo con las peticiones del ultimo minuto
    recientes = [hora for hora in visitas.get(ip, []) if ahora - hora < VENTANA_SEGUNDOS]

    if len(recientes) >= MAX_PETICIONES:
        return jsonify(error="Demasiadas peticiones"), 429, {"Retry-After": str(VENTANA_SEGUNDOS)}

    recientes.append(ahora)
    visitas[ip] = recientes


# ---------------------------------------------------------------
# Consultas a la base de datos
# ---------------------------------------------------------------
def buscar_peliculas(genero_id, saltar, limite):
    """Devuelve una pagina de peliculas, de mejor a peor puntuacion.
    Si viene genero_id, solo las de ese genero."""
    if genero_id:
        sql = f"""
            SELECT m.*, {GENEROS_DE_LA_PELICULA} AS generos
            FROM movies m
            JOIN movie_genres mg ON mg.movie_id = m.id
            WHERE mg.genre_id = %s
            ORDER BY m.rating DESC, m.id
            LIMIT %s OFFSET %s
        """
        return query(sql, (genero_id, limite, saltar))

    sql = f"""
        SELECT m.*, {GENEROS_DE_LA_PELICULA} AS generos
        FROM movies m
        ORDER BY m.rating DESC, m.id
        LIMIT %s OFFSET %s
    """
    return query(sql, (limite, saltar))


def contar_peliculas(genero_id):
    """Cuenta cuantas peliculas hay en total (sirve para saber cuantas paginas hay)."""
    if genero_id:
        sql = "SELECT COUNT(*) AS total FROM movie_genres WHERE genre_id = %s"
        return query(sql, (genero_id,))[0]["total"]

    return query("SELECT COUNT(*) AS total FROM movies")[0]["total"]


def peliculas_para_emocion(emocion_nombre):
    """Recomienda peliculas segun la emocion.

    Une 4 tablas con JOIN:  emotions -> emotion_genres -> movie_genres -> movies
    Pone primero las que coinciden con mas generos de la emocion y,
    si empatan, las de mejor puntuacion.
    """
    sql = f"""
        SELECT m.*, {GENEROS_DE_LA_PELICULA} AS generos,
               COUNT(DISTINCT eg.genre_id) AS coincidencias
        FROM emotions e
        JOIN emotion_genres eg ON eg.emotion_id = e.id
        JOIN movie_genres mg   ON mg.genre_id = eg.genre_id
        JOIN movies m          ON m.id = mg.movie_id
        WHERE e.name = %s
        GROUP BY m.id
        ORDER BY coincidencias DESC, m.rating DESC
        LIMIT 9
    """
    return query(sql, (emocion_nombre,))


# ---------------------------------------------------------------
# Endpoints (las "direcciones" de la API) 
# ---------------------------------------------------------------
@app.route("/api/peliculas")
def listar_peliculas():
    """Ejemplo: /api/peliculas?skip=0&limit=12&genero=35
    skip = cuantas peliculas saltar, limit = cuantas devolver."""
    genero_id = request.args.get("genero", type=int)
    saltar = request.args.get("skip", 0, type=int)
    limite = request.args.get("limit", PELICULAS_POR_PAGINA, type=int)

    # Evitamos valores raros: skip no negativo y limit entre 1 y 50
    saltar = max(saltar, 0)
    limite = max(1, min(limite, LIMITE_MAXIMO))

    total = contar_peliculas(genero_id)
    return jsonify(
        total=total,
        skip=saltar,
        limit=limite,
        tiene_mas=saltar + limite < total,
        items=buscar_peliculas(genero_id, saltar, limite),
    )


@app.route("/api/peliculas/<int:movie_id>")
def detalle_pelicula(movie_id):
    sql = f"SELECT m.*, {GENEROS_DE_LA_PELICULA} AS generos FROM movies m WHERE m.id = %s"
    resultado = query(sql, (movie_id,))
    if not resultado:
        abort(404)  # no existe esa pelicula
    return jsonify(resultado[0])


@app.route("/api/generos")
def listar_generos():
    return jsonify(query("SELECT * FROM genres ORDER BY name"))


@app.route("/api/emociones")
def listar_emociones():
    return jsonify(query("SELECT * FROM emotions"))


@app.route("/api/emocion", methods=["POST"])
def detectar():
    """Recibe {"texto": "estoy triste"} y devuelve la emocion detectada."""
    texto = (request.get_json(silent=True) or {}).get("texto", "")
    return jsonify(emocion=detectar_emocion(texto))


@app.route("/api/recomendar/<emocion>")
def recomendar_por_emocion(emocion):
    """Devuelve peliculas para una emocion (sin guardarla en el historial)."""
    return jsonify(peliculas_para_emocion(emocion))


@app.route("/api/recomendar", methods=["POST"])
def recomendar():
    """Recibe {"texto": "estoy triste"} o {"emocion": "triste"}.
    Detecta la emocion, la guarda en el historial y devuelve las peliculas."""
    datos = request.get_json(silent=True) or {}
    texto = (datos.get("texto") or "").strip()

    # Si no nos dicen la emocion, la detectamos a partir del texto
    nombre = datos.get("emocion") or detectar_emocion(texto)

    emocion = None
    if nombre:
        encontradas = query("SELECT * FROM emotions WHERE name = %s", (nombre,))
        if encontradas:
            emocion = encontradas[0]

    # No se detecto ninguna emocion: devolvemos las mejor puntuadas
    if emocion is None:
        return jsonify(emocion=None, peliculas=buscar_peliculas(None, 0, 6))

    # Guardamos la busqueda para las estadisticas
    sql = "INSERT INTO searches (text, emotion_id) VALUES (%s, %s)"
    query(sql, (texto or "(boton " + emocion["label"] + ")", emocion["id"]), commit=True)

    return jsonify(emocion=emocion, peliculas=peliculas_para_emocion(emocion["name"]))


@app.route("/api/estadisticas")
def estadisticas():
    """Cuantas veces se registro cada emocion en cada dia (para el grafico de barras).
    Ejemplo: /api/estadisticas?dias=30"""
    dias_atras = request.args.get("dias", 30, type=int)
    dias_atras = max(1, min(dias_atras, 365))

    # JOIN entre searches y emotions, contando por dia y por emocion
    filas = query("""
        SELECT DATE(s.created_at) AS dia, e.label, e.emoji, COUNT(*) AS total
        FROM searches s
        JOIN emotions e ON e.id = s.emotion_id
        WHERE s.created_at >= CURDATE() - INTERVAL %s DAY
        GROUP BY DATE(s.created_at), e.id
        ORDER BY dia
    """, (dias_atras - 1,))

    def nombre_del_dia(fecha):
        return f"{DIAS_SEMANA[fecha.weekday()]} {fecha:%d/%m}"   # ej: "sáb 14/11"

    # Lista de dias que tienen datos (eje X del grafico)
    dias = sorted({fila["dia"] for fila in filas})
    etiquetas = [nombre_del_dia(dia) for dia in dias]

    # Ordenamos los datos asi:  veces["Feliz"][dia] = 3
    veces = {}
    emojis = {}
    for fila in filas:
        veces.setdefault(fila["label"], {})[fila["dia"]] = fila["total"]
        emojis[fila["label"]] = fila["emoji"]

    series = []    # una serie de barras por cada emocion
    resumen = []   # el dia con mas registros de cada emocion
    for emocion, por_dia in veces.items():
        series.append({
            "label": f"{emojis[emocion]} {emocion}",
            "emocion": emocion,
            "data": [por_dia.get(dia, 0) for dia in dias],   # 0 si ese dia no hubo
        })

        mejor_dia = max(por_dia, key=por_dia.get)
        resumen.append({
            "emoji": emojis[emocion],
            "emocion": emocion,
            "dia": nombre_del_dia(mejor_dia),
            "veces": por_dia[mejor_dia],
            "total": sum(por_dia.values()),
        })

    resumen.sort(key=lambda r: r["total"], reverse=True)
    return jsonify(etiquetas=etiquetas, series=series, resumen=resumen, dias=dias_atras)


@app.route("/api/registro", methods=["POST"])
def registro():
    """Recibe {"usuario": "ana", "password": "1234"} y crea la cuenta."""
    datos = request.get_json(silent=True) or {}
    usuario = (datos.get("usuario") or "").strip()
    password = datos.get("password") or ""
    if not 3 <= len(usuario) <= 50 or len(password) < 4:
        return jsonify(error="Usuario de 3 a 50 caracteres y contraseña de al menos 4."), 400
    try:
        user_id = query("INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                        (usuario, generate_password_hash(password)), commit=True)
    except IntegrityError:
        return jsonify(error="Ese usuario ya existe."), 409
    return jsonify(id=user_id, usuario=usuario), 201


@app.route("/api/login", methods=["POST"])
def login():
    """Recibe {"usuario": "ana", "password": "1234"}. Devuelve el usuario o 401."""
    datos = request.get_json(silent=True) or {}
    filas = query("SELECT * FROM users WHERE username = %s", ((datos.get("usuario") or "").strip(),))
    if not filas or not check_password_hash(filas[0]["password_hash"], datos.get("password") or ""):
        return jsonify(error="Usuario o contraseña incorrectos."), 401
    return jsonify(id=filas[0]["id"], usuario=filas[0]["username"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
