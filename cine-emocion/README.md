# 🎬 CineEmoción – Recomendador de películas según tu emoción

Proyecto universitario con **frontend y backend separados**, ambos en **Flask**, y base de datos **MySQL**.
El usuario escribe cómo se siente (o pulsa una emoción), el backend detecta la emoción por palabras clave
y recomienda películas según los géneros asociados a esa emoción.

```
Navegador ──► FRONTEND (Flask, :5000) ──HTTP/JSON──► BACKEND (Flask API, :5001) ──► MySQL (:3306)
```

## Estructura
```
cine-emocion/
├── docker-compose.yml        MySQL listo para usar (carga backend/sql/*.sql)
├── requirements.txt          instala backend + frontend de una vez
├── backend/                  API REST + base de datos
│   ├── app.py                endpoints JSON, paginado (skip/limit) y rate limit
│   ├── db.py, config.py      conexión MySQL (PyMySQL) y variables de entorno
│   ├── emotion.py            detector de emoción por palabras clave
│   ├── sql/                  schema.sql y seeds (100 películas)
│   └── static/posters/       imágenes de los pósters
└── frontend/                 sitio web
    ├── app.py                páginas; pide los datos al backend con requests
    ├── templates/            HTML (Jinja2)
    └── static/               CSS y Chart.js
```

## Modelo de datos y JOINs
```
movies ──< movie_genres >── genres ──< emotion_genres >── emotions ──< searches
```
- **Catálogo**: `movies JOIN movie_genres JOIN genres` (géneros de cada película).
- **Recomendación**: `emotions JOIN emotion_genres JOIN movie_genres JOIN movies`,
  ordenado por cantidad de géneros coincidentes y puntuación.
- **Estadísticas**: `searches JOIN emotions` + `GROUP BY` día y emoción (gráfico de barras).

## Cómo ejecutarlo
1. Base de datos: `docker compose up -d`
   (o con MySQL local: cargar en orden `backend/sql/schema.sql`, `seed.sql`, `seed_extra.sql`, `seed_extra2.sql`, `seed_extra3.sql`, `seed_users.sql`)
2. Entorno Python (una sola vez):
   ```bash
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   cp backend/.env.example backend/.env      # ajusta usuario/clave de MySQL
   cp frontend/.env.example frontend/.env
   ```
3. Backend (terminal 1):  `cd backend && python app.py`   → http://127.0.0.1:5001
4. Frontend (terminal 2): `cd frontend && python app.py`  → **http://127.0.0.1:5000**

## Endpoints del backend
| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/peliculas?skip=0&limit=12&genero=35` | catálogo paginado (`total`, `tiene_mas`, `items`) |
| GET | `/api/peliculas/<id>` | detalle de una película |
| GET | `/api/generos`, `/api/emociones` | listas auxiliares |
| POST | `/api/recomendar` | `{"texto": "estoy triste"}` o `{"emocion": "triste"}`; guarda en el historial |
| GET | `/api/recomendar/<emocion>` | recomendación sin guardar historial |
| POST | `/api/emocion` | `{"texto": "..."}` → emoción detectada |
| GET | `/api/estadisticas?dias=30` | datos para el gráfico por día |

Rate limit: 60–120 peticiones por minuto por IP (responde `429` con `Retry-After`).

## Pósters
Las imágenes ya están descargadas en `backend/static/posters/` y la tabla `movies` guarda su ruta en `poster_url`.

## Datos de ejemplo para el gráfico (opcional)
`backend/sql/seed_demo_busquedas.sql` inserta búsquedas ficticias (`[demo]`).
Para borrarlas: `DELETE FROM searches WHERE text LIKE '[demo]%';`

## Login
Usuario precargado: **demo** / **demo1234**. Desde `/registro` se pueden crear más (no permite usuarios repetidos).
