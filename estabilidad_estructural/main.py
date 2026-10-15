#!/usr/bin/env python3
"""
Punto de entrada del programa.
Ejercicio 8: Analisis de Estabilidad Estructural en Ingenieria Civil
Victoria Correa 30430255
Helena pena 30204443

"""

from matriz_rigidez import MatrizRigidez
from analisis_critico import AnalisisCritico
from reporte_estructural import ReporteEstructural


def ejecutar_analisis_estructural(filas, columnas, nombre_archivo):
    """Construye la matriz, la analiza y genera el reporte final."""

    matriz = MatrizRigidez(filas, columnas)
    matriz.construir()

    print("Matriz de rigidez estructural:")
    for fila in matriz.datos:
        print(fila)

    analisis = AnalisisCritico(matriz)

    analisis.extraer_diagonal()
    print(f"\nVector de analisis (diagonal principal): {analisis.vector_analisis}")

    analisis.ordenar_puntos_criticos()
    print(f"\nPuntos criticos de deformacion (mayor a menor): {analisis.puntos_ordenados}")

    print()
    reporte = ReporteEstructural(matriz, analisis)
    reporte.mostrar()
    reporte.guardar(nombre_archivo)


def probar_datos_invalidos():
    """Demuestra que el programa maneja datos invalidos sin romperse."""

    print("\n--- Probando con datos invalidos ---")
    try:
        MatrizRigidez(-3, 5)
    except (ValueError, TypeError) as e:
        print(f"Error controlado al crear la matriz: {e}")

    matriz_vacia = MatrizRigidez(3, 3)
    analisis_vacio = AnalisisCritico(matriz_vacia)
    analisis_vacio.extraer_diagonal()
    analisis_vacio.ordenar_puntos_criticos()


if __name__ == "__main__":
    try:
        ejecutar_analisis_estructural(filas=3, columnas=3, nombre_archivo="resultados_estructura.txt")
    except Exception as e:
        print(f"Error inesperado en el analisis estructural: {e}")

    probar_datos_invalidos()
