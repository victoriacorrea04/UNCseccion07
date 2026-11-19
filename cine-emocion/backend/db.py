import pymysql
from pymysql.cursors import DictCursor
from config import DB_CONFIG


def query(sql, params=None, commit=False):
    """Ejecuta una consulta y devuelve las filas como diccionarios."""
    conn = pymysql.connect(cursorclass=DictCursor, **DB_CONFIG)
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params or ())
            if commit:
                conn.commit()
                return cur.lastrowid
            return cur.fetchall()
    finally:
        conn.close()
