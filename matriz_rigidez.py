#!/usr/bin/env python3
"""
Modulo con la clase MatrizRigidez: construccion de la matriz NxM de
coeficientes de rigidez estructural a partir de datos ingresados por el usuario.
"""


class MatrizRigidez:
    """Representa la matriz de coeficientes de rigidez de una estructura."""

    def __init__(self, filas, columnas):
        # self equivale al "this" de otros lenguajes: hace referencia al propio objeto
        self._filas = None
        self._columnas = None
        self._datos = []

        self.filas = filas
        self.columnas = columnas

    # ---------- Properties (encapsulan filas y columnas con validacion) ----------

    @property
    def filas(self):
        return self._filas

    @filas.setter
    def filas(self, valor):
        try:
            if valor <= 0:
                raise ValueError("El numero de filas debe ser positivo")
            self._filas = valor
        except TypeError:
            raise TypeError("El numero de filas debe ser un entero")

    @property
    def columnas(self):
        return self._columnas

    @columnas.setter
    def columnas(self, valor):
        try:
            if valor <= 0:
                raise ValueError("El numero de columnas debe ser positivo")
            self._columnas = valor
        except TypeError:
            raise TypeError("El numero de columnas debe ser un entero")

    @property
    def datos(self):
        return self._datos

    # ---------- Metodos principales ----------

    def construir(self):
        """Construye la matriz NxM pidiendo al usuario cada coeficiente de rigidez."""
        try:
            matriz = []
            for i in range(self.filas):
                fila = []
                for j in range(self.columnas):
                    while True:
                        try:
                            dato = input(
                                f"Ingrese el coeficiente de rigidez para la posicion "
                                f"[{i}][{j}] (ejemplo: 250.5): "
                            )
                            coeficiente = float(dato)
                            break
                        except ValueError:
                            print("Valor invalido. Debe ingresar un numero, ejemplo: 250.5")
                    fila.append(coeficiente)
                matriz.append(fila)

            self._datos = matriz
            return self._datos

        except Exception as e:
            print(f"Error al construir la matriz de rigidez: {e}")
            return None
