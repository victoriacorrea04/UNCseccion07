"""Detector de emociones muy simple basado en palabras clave."""
import unicodedata

KEYWORDS = {
    "feliz": ["feliz", "contento", "alegre", "genial", "bien", "animado", "emocionado", "happy"],
    "triste": ["triste", "deprimido", "llorar", "mal", "solo", "sola", "melancolico", "pena", "sad"],
    "enojado": ["enojado", "furioso", "rabia", "molesto", "enfadado", "ira", "bronca", "angry"],
    "ansioso": ["ansioso", "estres", "estresado", "nervioso", "preocupado", "agobiado", "ansiedad"],
    "aburrido": ["aburrido", "aburrimiento", "nada que hacer", "monotonia", "bored"],
    "romantico": ["romantico", "enamorado", "amor", "cita", "pareja", "love"],
}


def normalizar(texto):
    """Pasa a minusculas y quita tildes."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def detectar_emocion(texto):
    """Devuelve el nombre de la emocion con mas coincidencias, o None."""
    texto = normalizar(texto)
    mejor, mejor_puntos = None, 0
    for emocion, palabras in KEYWORDS.items():
        puntos = sum(1 for p in palabras if p in texto)
        if puntos > mejor_puntos:
            mejor, mejor_puntos = emocion, puntos
    return mejor
