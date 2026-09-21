# Victoria Correa 30430255, Helena Peña 30204443. Sección 07
"""
Enunciado 10: Robots de Soldadura

Descripción:
Clase base RobotSoldador con:
• Atributo privado __modelo
• Atributo protegido _temperatura
• Método soldar() -> "El robot suelda una pieza".

Clases hijas:
• SoldadorPunto -> sobrescribe soldar() -> "⚡ Soldando por puntos".
• SoldadorArco -> sobrescribe soldar() -> "🔥 Soldando por arco eléctrico".

Requisitos:
• Encapsula el modelo con @property.
• Usa super().__init__() en las hijas.
• Crea un objeto de cada clase y llama a soldar().
"""

from abc import ABC, abstractmethod

class RobotSoldador(ABC):
    """Clase base para robots de soldadura."""

    def __init__(self, modelo):
        self.__modelo = modelo
        self._temperatura = 0

    @property
    def modelo(self):
        return self.__modelo

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        self._temperatura = valor

    def soldar(self):
        return "El robot suelda una pieza"


class SoldadorPunto(RobotSoldador):
    """Robot que suelda por puntos."""

    def __init__(self, modelo):
        super().__init__(modelo)
        self._temperatura = 1500

    def soldar(self):
        return "⚡ Soldando por puntos"


class SoldadorArco(RobotSoldador):
    """Robot que suelda por arco eléctrico."""

    def __init__(self, modelo):
        super().__init__(modelo)
        self._temperatura = 1800

    def soldar(self):
        return "🔥 Soldando por arco eléctrico"


# Crear un objeto de cada clase y llamar a soldar()
if __name__ == "__main__":
    soldador_punto = SoldadorPunto("FANUC ARC Mate 100iD")
    soldador_arco = SoldadorArco("KUKA KR QUANTEC")

    print("\n>>> ENUNCIADO 10: ROBOTS DE SOLDADURA\n")

    print("\n[SOLDADOR POR PUNTOS]")
    print(f"Modelo: {soldador_punto.modelo}")
    print(soldador_punto.soldar())
    print(f"Temperatura: {soldador_punto.temperatura}°C")

    print("\n[SOLDADOR POR ARCO ELÉCTRICO]")
    print(f"Modelo: {soldador_arco.modelo}")
    print(soldador_arco.soldar())
    print(f"Temperatura: {soldador_arco.temperatura}°C\n")
