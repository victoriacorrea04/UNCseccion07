#!/usr/bin/env python3
"""
Modulo con la clase ReporteEstructural: genera, muestra y guarda el reporte
formal del analisis de estabilidad estructural.
"""


class ReporteEstructural:
    """Genera el reporte a partir de una MatrizRigidez y un AnalisisCritico."""

    def __init__(self, matriz_rigidez, analisis_critico):
        # self equivale al "this" de otros lenguajes: hace referencia al propio objeto
        self._matriz_rigidez = matriz_rigidez
        self._analisis_critico = analisis_critico

    # ---------- Metodos principales ----------

    def _generar_texto(self):
        """Arma el texto del reporte formal a partir de la matriz y los vectores procesados."""
        if not self._matriz_rigidez.datos:
            raise ValueError("Primero se debe construir la matriz de rigidez")

        lineas = []
        lineas.append("REPORTE DE ANALISIS DE ESTABILIDAD ESTRUCTURAL")
        lineas.append("=" * 48)
        lineas.append(
            f"\nDimensiones de la matriz: "
            f"{self._matriz_rigidez.filas} x {self._matriz_rigidez.columnas}\n"
        )

        lineas.append("Matriz de coeficientes de rigidez:")
        for fila in self._matriz_rigidez.datos:
            valores = "  ".join(f"{valor:>10.2f}" for valor in fila)
            lineas.append(f"  {valores}")

        lineas.append("\nVector de analisis (diagonal principal):")
        lineas.append(f"  {self._analisis_critico.vector_analisis}")

        lineas.append("\nPuntos criticos de deformacion (mayor a menor):")
        lineas.append(f"  {self._analisis_critico.puntos_ordenados}")

        return "\n".join(lineas)

    def mostrar(self):
        """Imprime en pantalla el reporte formal."""
        try:
            print(self._generar_texto())
        except ValueError as e:
            print(f"Error al mostrar el reporte: {e}")

    def guardar(self, nombre_archivo):
        """Guarda el reporte formal en un archivo externo .txt."""
        try:
            texto_reporte = self._generar_texto()
            with open(nombre_archivo, "w") as archivo:
                archivo.write(texto_reporte + "\n")

            print(f"Resultados guardados en '{nombre_archivo}'")

        except ValueError as e:
            print(f"Error al guardar el archivo: {e}")
        except (IOError, OSError) as e:
            print(f"Error al guardar el archivo: {e}")
