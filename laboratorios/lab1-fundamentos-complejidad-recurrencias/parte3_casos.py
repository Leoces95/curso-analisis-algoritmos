"""Ejecución de experimentos para la Parte 3 y generación de gráficas."""

import os
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMAÑOS = [100, 200, 400, 800, 1600, 3200, 6400]


def ejecutar_experimento_p3():
    os.makedirs("graficas", exist_ok=True)

    tiempos = {"A": [], "B": [], "C": []}
    comparaciones = {"A": [], "B": [], "C": []}

    for n in TAMAÑOS:
        # Escenario A (Caso Promedio)
        datos_a = generar_aleatorio(n)
        t0 = time.perf_counter()
        _, comps_a = insertion_sort(datos_a)
        t1 = time.perf_counter()
        tiempos["A"].append(t1 - t0)
        comparaciones["A"].append(comps_a)

        # Escenario B (Mejor Caso Práctico / Casi Ordenado)
        datos_b = generar_casi_ordenado(n)
        t0 = time.perf_counter()
        _, comps_b = insertion_sort(datos_b)
        t1 = time.perf_counter()
        tiempos["B"].append(t1 - t0)
        comparaciones["B"].append(comps_b)

        # Escenario C (Peor Caso)
        datos_c = generar_inverso(n)
        t0 = time.perf_counter()
        _, comps_c = insertion_sort(datos_c)
        t1 = time.perf_counter()
        tiempos["C"].append(t1 - t0)
        comparaciones["C"].append(comps_c)

    # Gráfica 1: Comparaciones vs Tamaño
    plt.figure(figsize=(8, 5))
    plt.plot(TAMAÑOS, comparaciones["A"], label="Escenario A (Aleatorio)", marker="o")
    plt.plot(TAMAÑOS, comparaciones["B"], label="Escenario B (Casi Ordenado)", marker="s")
    plt.plot(TAMAÑOS, comparaciones["C"], label="Escenario C (Inverso)", marker="^")
    plt.title("Insertion Sort: Comparaciones vs. Tamaño de Entrada")
    plt.xlabel("Tamaño de Entrada (n) [registros]")
    plt.ylabel("Número de Comparaciones [operaciones]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Gráfica 2: Tiempo vs Tamaño
    plt.figure(figsize=(8, 5))
    plt.plot(TAMAÑOS, tiempos["A"], label="Escenario A (Aleatorio)", marker="o")
    plt.plot(TAMAÑOS, tiempos["B"], label="Escenario B (Casi Ordenado)", marker="s")
    plt.plot(TAMAÑOS, tiempos["C"], label="Escenario C (Inverso)", marker="^")
    plt.title("Insertion Sort: Tiempo de Ejecución vs. Tamaño de Entrada")
    plt.xlabel("Tamaño de Entrada (n) [registros]")
    plt.ylabel("Tiempo de Ejecución [segundos]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_experimento_p3()