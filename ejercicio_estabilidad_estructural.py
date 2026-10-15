#!/usr/bin/env python3
"""
Ejercicio 8: Analisis de Estabilidad Estructural en Ingenieria Civil
Matriz de rigidez, vector de diagonal (puntos criticos) y persistencia en archivo.
"""
# Victoria Correa 30430255 
# Helena Peña 30204443
# Seccion 07

class AnalisisEstructural:
    """Representa el analisis de rigidez de una estructura mediante matrices."""

    def __init__(self, filas, columnas):
        
        self._filas = None
        self._columnas = None
        self._matriz_rigidez = []
        self._vector_analisis = []
        self._puntos_ordenados = []

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
    def matriz_rigidez(self):
        return self._matriz_rigidez

    @property
    def vector_analisis(self):
        return self._vector_analisis

    @property
    def puntos_ordenados(self):
        return self._puntos_ordenados

    # ---------- Metodos principales del reto ----------

    def construir_matriz_rigidez(self):
        """Construye una matriz NxM pidiendo al usuario cada coeficiente de rigidez."""
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

            self._matriz_rigidez = matriz
            return self._matriz_rigidez

        except Exception as e:
            print(f"Error al construir la matriz de rigidez: {e}")
            return None

    def extraer_diagonal(self):
        """Extrae los elementos de la diagonal principal hacia el vector de analisis."""
        try:
            if not self._matriz_rigidez:
                raise ValueError("Primero se debe construir la matriz de rigidez")

            vector = []
            limite = min(self.filas, self.columnas)

            for i in range(limite):
                vector.append(self._matriz_rigidez[i][i])

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

    def _generar_texto_reporte(self):
        """Arma el texto del reporte formal a partir de la matriz y los vectores procesados."""
        if not self._matriz_rigidez:
            raise ValueError("Primero se debe construir la matriz de rigidez")

        lineas = []
        lineas.append("REPORTE DE ANALISIS DE ESTABILIDAD ESTRUCTURAL")
        lineas.append("=" * 48)
        lineas.append(f"\nDimensiones de la matriz: {self.filas} x {self.columnas}\n")

        lineas.append("Matriz de coeficientes de rigidez:")
        for fila in self._matriz_rigidez:
            valores = "  ".join(f"{valor:>10.2f}" for valor in fila)
            lineas.append(f"  {valores}")

        lineas.append("\nVector de analisis (diagonal principal):")
        lineas.append(f"  {self._vector_analisis}")

        lineas.append("\nPuntos criticos de deformacion (mayor a menor):")
        lineas.append(f"  {self._puntos_ordenados}")

        return "\n".join(lineas)

    def mostrar_reporte(self):
        """Imprime en pantalla el reporte formal."""
        try:
            print(self._generar_texto_reporte())
        except ValueError as e:
            print(f"Error al mostrar el reporte: {e}")

    def guardar_resultados(self, nombre_archivo):
        """Guarda el reporte formal en un archivo externo .txt."""
        try:
            texto_reporte = self._generar_texto_reporte()
            with open(nombre_archivo, "w") as archivo:
                archivo.write(texto_reporte + "\n")

            print(f"Resultados guardados en '{nombre_archivo}'")

        except ValueError as e:
            print(f"Error al guardar el archivo: {e}")
        except (IOError, OSError) as e:
            print(f"Error al guardar el archivo: {e}")


# ---------------------- Programa principal ----------------------

if __name__ == "__main__":

    try:
        N = 3
        M = 3

        analisis = AnalisisEstructural(N, M)

        analisis.construir_matriz_rigidez()
        print("Matriz de rigidez estructural:")
        for fila in analisis.matriz_rigidez:
            print(fila)

        analisis.extraer_diagonal()
        print(f"\nVector de analisis (diagonal principal): {analisis.vector_analisis}")

        analisis.ordenar_puntos_criticos()
        print(f"\nPuntos criticos de deformacion (mayor a menor): {analisis.puntos_ordenados}")

        print()
        analisis.mostrar_reporte()

        analisis.guardar_resultados("resultados_estructura.txt")

    except Exception as e:
        print(f"Error inesperado en el analisis estructural: {e}")

    print("\n--- Probando con datos invalidos ---")
    try:
        analisis_invalido = AnalisisEstructural(-3, 5)
    except (ValueError, TypeError) as e:
        print(f"Error controlado al crear el analisis: {e}")

    analisis_vacio = AnalisisEstructural(3, 3)
    analisis_vacio.extraer_diagonal()
    analisis_vacio.ordenar_puntos_criticos()
