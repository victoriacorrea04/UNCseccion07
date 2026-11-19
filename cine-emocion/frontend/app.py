"""FRONTEND: sitio web en Flask (plantillas Jinja2). No toca la base de datos:
todos los datos los pide por HTTP al backend (API REST).

Puerto 5000.  Variable de entorno BACKEND_URL (por defecto http://127.0.0.1:5001).
"""
import os

import requests
from dotenv import load_dotenv
from urllib.parse import quote

from flask import Flask, has_request_context, redirect, render_template, request, url_for

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5001").rstrip("/")
POR_PAGINA = 12

app = Flask(__name__)


def usuario_actual():
    """Usuario que viene en la URL (?u=ana). Sin cookies: el nombre viaja en cada enlace."""
    return (request.args.get("u") or "").strip() or None if has_request_context() else None


@app.url_defaults
def conservar_usuario(endpoint, values):
    """Agrega ?u=<usuario> a todos los url_for(...) para no perder quien esta navegando.
    Para quitarlo (ej. al salir) se usa url_for(..., u=None)."""
    if endpoint != "static" and "u" not in values and usuario_actual():
        values["u"] = usuario_actual()


def api(ruta, metodo="GET", **kwargs):
    """Llama al backend y devuelve el JSON. Lanza ErrorBackend si falla."""
    try:
        r = requests.request(metodo, f"{BACKEND_URL}{ruta}", timeout=10, **kwargs)
    except requests.RequestException:
        raise ErrorBackend("No se pudo conectar con el backend. ¿Está encendido en " + BACKEND_URL + "?")
    if r.status_code == 429:
        raise ErrorBackend("Demasiadas peticiones, espera un momento e inténtalo de nuevo.")
    if r.status_code in (400, 401, 409):
        raise ErrorLogin(r.json().get("error", "Error"))
    if r.status_code == 404:
        raise ErrorBackend("No encontrado.", 404)
    r.raise_for_status()
    return r.json()


class ErrorLogin(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class ErrorBackend(Exception):
    def __init__(self, mensaje, codigo=503):
        self.mensaje, self.codigo = mensaje, codigo


@app.errorhandler(ErrorBackend)
def error_backend(e):
    return render_template("error.html", mensaje=e.mensaje), e.codigo


@app.template_filter("poster")
def poster(url):
    """Los posters viven en el backend: convierte '/static/posters/1.jpg' en URL completa."""
    return f"{BACKEND_URL}{url}" if url and url.startswith("/") else url


@app.route("/catalogo")
def index():
    genero_id = request.args.get("genero", type=int)
    pagina = max(request.args.get("pagina", 1, type=int), 1)
    params = {"limit": POR_PAGINA, "skip": (pagina - 1) * POR_PAGINA}
    if genero_id:
        params["genero"] = genero_id
    datos = api("/api/peliculas", params=params)
    paginas = max((datos["total"] + POR_PAGINA - 1) // POR_PAGINA, 1)
    if pagina > paginas:  # pagina fuera de rango: vuelve a pedir la ultima
        pagina = paginas
        params["skip"] = (pagina - 1) * POR_PAGINA
        datos = api("/api/peliculas", params=params)
    return render_template("index.html", peliculas=datos["items"], total=datos["total"],
                           pagina=pagina, paginas=paginas, genero_id=genero_id,
                           generos=api("/api/generos"), emociones=api("/api/emociones"))


@app.route("/recomendar", methods=["GET", "POST"])
def recomendar():
    texto = request.form.get("texto", "").strip()
    cuerpo = {"emocion": request.args["emocion"]} if request.args.get("emocion") else {"texto": texto}
    cuerpo["usuario"] = usuario_actual()
    datos = api("/api/recomendar", "POST", json=cuerpo)
    return render_template("recomendacion.html", emocion=datos["emocion"], texto=texto,
                           peliculas=datos["peliculas"], personalizada=datos.get("personalizada"))


@app.route("/pelicula/<int:movie_id>")
def pelicula(movie_id):
    return render_template("pelicula.html", p=api(f"/api/peliculas/{movie_id}"))


def ruta_preferencias(usuario):
    return f"/api/usuarios/{quote(usuario, safe='')}/preferencias"


@app.route("/estadisticas")
def estadisticas():
    """Estadisticas del usuario (?u=ana). Con ?todos=1 se ven las de todos."""
    usuario = None if request.args.get("todos") else usuario_actual()
    params = {"dias": request.args.get("dias", 30, type=int)}
    if usuario:
        params["usuario"] = usuario
    datos = api("/api/estadisticas", params=params)

    preferencias = None
    if usuario:   # preferencias del usuario, con el nombre de cada genero
        ids = api(ruta_preferencias(usuario))
        nombres = {g["id"]: g["name"] for g in api("/api/generos")}
        preferencias = {tipo: [nombres[i] for i in ids[tipo]] for tipo in ("gusta", "evita")}
    return render_template("estadisticas.html", etiquetas=datos["etiquetas"], series=datos["series"],
                           resumen=datos["resumen"], dias_atras=datos["dias"],
                           propias=bool(usuario), preferencias=preferencias)


@app.route("/hoy", methods=["GET", "POST"])
def hoy():
    """Cuestionario '¿Como te sientes hoy?': emocion + generos que le gustan / evita."""
    usuario = usuario_actual()
    if not usuario:
        return redirect(url_for("login"))
    ruta = ruta_preferencias(usuario)
    try:
        preferencias = api(ruta)
    except ErrorBackend as e:
        if e.codigo == 404:   # el usuario no existe: de vuelta al login
            return redirect(url_for("login", u=None))
        raise

    error, elegida = None, request.form.get("emocion")
    if request.method == "POST":
        gusta = request.form.getlist("gusta", type=int)
        evita = request.form.getlist("evita", type=int)
        preferencias = {"gusta": gusta, "evita": evita}
        if not elegida:
            error = "Elige cómo te sientes hoy."
        else:
            try:
                api(ruta, "PUT", json=preferencias)
                return redirect(url_for("recomendar", emocion=elegida))
            except ErrorLogin as e:
                error = e.mensaje
    return render_template("hoy.html", usuario=usuario, error=error, elegida=elegida,
                           preferencias=preferencias, emociones=api("/api/emociones"),
                           generos=api("/api/generos"))


def posters_del_sistema():
    """Posters de las mejor puntuadas para el mosaico de la pantalla de login."""
    try:
        peliculas = api("/api/peliculas", params={"limit": 12})["items"]
    except ErrorBackend:
        return []   # sin backend el login igual se ve (con el fondo de color)
    return [p["poster_url"] for p in peliculas if p["poster_url"]]


def formulario_cuenta(ruta, plantilla):
    """Login y registro comparten el flujo: enviar usuario/password al backend."""
    error = None
    if request.method == "POST":
        cuerpo = {"usuario": request.form.get("usuario", ""),
                  "password": request.form.get("password", "")}
        try:
            datos = api(ruta, "POST", json=cuerpo)
            if ruta == "/api/registro":   # tras registrarse, inicia sesion
                datos = api("/api/login", "POST", json=cuerpo)
            return redirect(url_for("hoy", u=datos["usuario"]))   # tras entrar: cuestionario
        except ErrorLogin as e:
            error = e.mensaje
    return render_template(plantilla, error=error, posters=posters_del_sistema())


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    return formulario_cuenta("/api/login", "login.html")


@app.route("/registro", methods=["GET", "POST"])
def registro():
    return formulario_cuenta("/api/registro", "registro.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
