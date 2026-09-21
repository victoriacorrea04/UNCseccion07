# Victoria Correa 30430255, Helena Peña 30204443. Sección 07
"""
Enunciado 3: Brazos Robóticos

Descripción:
Clase base BrazoRobotico con:
• Atributo privado __modelo
• Atributo protegido _grados_libertad
• Método mover() -> "El brazo se mueve".

Clases hijas:
• BrazoArticulado -> sobrescribe mover() -> "💪 Brazo articulado moviéndose en 6 ejes".
• BrazoCartesiano -> sobrescribe mover() -> "📐 Brazo cartesiano moviéndose en X, Y, Z".

Requisitos:
• Usa @property para el modelo.
• Usa super().__init__() en las hijas.
• Crea un objeto de cada clase y llama a mover().
"""

from abc import ABC, abstractmethod

class BrazoRobotico(ABC):
    """Clase base para brazos robóticos."""

    def __init__(self, modelo):
        self.__modelo = modelo
        self._grados_libertad = 0

    @property
    def modelo(self):
        return self.__modelo

    @property
    def grados_libertad(self):
        return self._grados_libertad

    @grados_libertad.setter
    def grados_libertad(self, valor):
        self._grados_libertad = valor

    def mover(self):
        return "El brazo se mueve"


class BrazoArticulado(BrazoRobotico):
    """Brazo articulado que se mueve en 6 ejes."""

    def __init__(self, modelo):
        super().__init__(modelo)
        self._grados_libertad = 6

    def mover(self):
        return "🤖 Brazo articulado moviéndose en 6 ejes"


class BrazoCartesiano(BrazoRobotico):
    """Brazo cartesiano que se mueve en X, Y, Z."""

    def __init__(self, modelo):
        super().__init__(modelo)
        self._grados_libertad = 3

    def mover(self):
        return "🦾 Brazo cartesiano moviéndose en X, Y, Z"


# Crear un objeto de cada clase y llamar a mover()
if __name__ == "__main__":
    brazo_articulado = BrazoArticulado("ABB IRB 6700")
    brazo_cartesiano = BrazoCartesiano("SCARA XYZ-1000")

    print("\n>>> ENUNCIADO 3: BRAZOS ROBÓTICOS\n")

    print("\n[BRAZO ARTICULADO]")
    print(f"Modelo: {brazo_articulado.modelo}")
    print(brazo_articulado.mover())
    print(f"Grados de libertad: {brazo_articulado.grados_libertad}")

    print("\n[BRAZO CARTESIANO]")
    print(f"Modelo: {brazo_cartesiano.modelo}")
    print(brazo_cartesiano.mover())
    print(f"Grados de libertad: {brazo_cartesiano.grados_libertad}\n")
