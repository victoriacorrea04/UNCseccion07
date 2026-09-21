# Victoria Correa 30430255, Helena Peña 30204443. Sección 07
"""
Enunciado 7: Sistemas de Visión

Descripción:
Clase base Camara con:
• Atributo privado __resolucion
• Atributo protegido _encendida (inicia en False)
• Método capturar() -> "Capturando imagen genérica".

Clases hijas:
• CamaraRGB -> sobrescribe capturar() -> "📷 Capturando imagen a color".
• CamaraInfrarroja -> sobrescribe capturar() -> "📉 Capturando imagen térmica".

Requisitos:
• Encapsula la resolución con @property.
• Crea un objeto de cada clase y llama a capturar().
"""

from abc import ABC, abstractmethod

class Camara(ABC):
    """Clase base para cámaras."""

    def __init__(self, resolucion):
        self.__resolucion = resolucion
        self._encendida = False

    @property
    def resolucion(self):
        return self.__resolucion

    @property
    def encendida(self):
        return self._encendida

    @encendida.setter
    def encendida(self, valor):
        self._encendida = valor

    def capturar(self):
        return "Capturando imagen genérica"


class CamaraRGB(Camara):
    """Cámara RGB que captura imágenes a color."""

    def __init__(self, resolucion):
        super().__init__(resolucion)

    def capturar(self):
        return "📷 Capturando imagen a color"


class CamaraInfrarroja(Camara):
    """Cámara infrarroja que captura imágenes térmicas."""

    def __init__(self, resolucion):
        super().__init__(resolucion)

    def capturar(self):
        return "🌡️ Capturando imagen térmica"


# Crear un objeto de cada clase y llamar a capturar()
if __name__ == "__main__":
    camara_rgb = CamaraRGB("1920x1080")
    camara_infrarroja = CamaraInfrarroja("640x480")

    print("\n>>> ENUNCIADO 7: SISTEMAS DE VISIÓN\n")

    print("\n[CÁMARA RGB]")
    print(f"Resolución: {camara_rgb.resolucion}")
    print(camara_rgb.capturar())
    print(f"Estado: {'Encendida' if camara_rgb.encendida else 'Apagada'}")

    print("\n[CÁMARA INFRARROJA]")
    print(f"Resolución: {camara_infrarroja.resolucion}")
    print(camara_infrarroja.capturar())
    print(f"Estado: {'Encendida' if camara_infrarroja.encendida else 'Apagada'}\n")
