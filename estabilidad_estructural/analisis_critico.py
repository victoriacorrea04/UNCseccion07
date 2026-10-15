#!/usr/bin/env python3
"""
Modulo con la clase AnalisisCritico: extraccion de la diagonal principal de
una matriz de rigidez y ordenamiento de los puntos criticos de deformacion.
"""


class AnalisisCritico:
    """Procesa una MatrizRigidez para obtener y ordenar sus puntos criticos."""

    def __init__(self, matriz_rigidez):
        # self equivale al "this" de otros lenguajes: hace referencia al propio objeto
        self._matriz_rigidez = matriz_rigidez
        self._vector_analisis = []
        self._puntos_ordenados = []

    # ---------- Properties ----------

    @property
    def vector_analisis(self):
        return self._vector_analisis

    @property
    def puntos_ordenados(self):
        return self._puntos_ordenados

    # ---------- Metodos principales ----------

    def extraer_diagonal(self):
        """Extrae los elementos de la diagonal principal hacia el vector de analisis."""
        try:
            if not self._matriz_rigidez.datos:
                raise ValueError("Primero se debe construir la matriz de rigidez")

            vector = []
            limite = min(self._matriz_rigidez.filas, self._matriz_rigidez.columnas)

            for i in range(limite):
                vector.append(self._matriz_rigidez.datos[i][i])

            self._vector_analisis = vector
            return self._vector_analisis

        except (ValueError, IndexError) as e:
            print(f"Error al extraer la diagonal: {e}")
            return None

    def ordenar_puntos_criticos(self):
        """
        Ordena los puntos criticos de deformacion de mayor a menor,
        usando una seleccion sucesiva de maximos con la funcion max().
        """
        try:
            if not self._vector_analisis:
                raise ValueError("El vector de analisis esta vacio")

            pendientes = list(self._vector_analisis)
            ordenado = []

            while pendientes:
                mayor = max(pendientes)
                ordenado.append(mayor)
                pendientes.remove(mayor)

            self._puntos_ordenados = ordenado
            return self._puntos_ordenados

        except ValueError as e:
            print(f"Error al ordenar los puntos criticos: {e}")
            return None
