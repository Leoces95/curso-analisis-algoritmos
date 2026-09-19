"""Ejecución de experimentos para la Parte 4 y generación de gráficas comparativas."""

import os
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMAÑOS = [100, 200, 400, 800, 1600, 3200, 6400]


def ejecutar_experimento_p4():
    os.makedirs("graficas", exist_ok=True)

    tiempos_insertion = []
    tiempos_merge = []

    for n in TAMAÑOS:
        datos = generar_aleatorio(n)

        # Insertion Sort
        t0 = time.perf_counter()
        insertion_sort(datos)
        t1 = time.perf_counter()
        tiempos_insertion.append(t1 - t0)

        # Merge Sort
        t0 = time.perf_counter()
        merge_sort(datos)
        t1 = time.perf_counter()
        tiempos_merge.append(t1 - t0)

    # Gráfica Comparativa: Tiempo vs Tamaño
    plt.figure(figsize=(8, 5))
    plt.plot(TAMAÑOS, tiempos_insertion, label="Insertion Sort", marker="o", color="red")
    plt.plot(TAMAÑOS, tiempos_merge, label="Merge Sort", marker="s", color="blue")
    plt.title("Comparación de Tiempo: Insertion Sort vs. Merge Sort (Escenario A)")
    plt.xlabel("Tamaño de Entrada (n) [registros]")
    plt.ylabel("Tiempo de Ejecución [segundos]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_experimento_p4()