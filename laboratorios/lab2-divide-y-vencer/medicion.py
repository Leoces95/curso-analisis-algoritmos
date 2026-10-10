"""Script de medición de tiempos de ejecución y generación de gráfica comparativa. """

import os
import random
import time
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempos() -> tuple[list[int], list[float], list[float]]:
    """Mide el tiempo promedio de ejecución para distintos tamaños de entrada n.

    Returns:
        Una tupla con las listas de tamaños, tiempos de fuerza bruta y tiempos de divide y vencerás.
    """
    tamanios = [10, 50, 100, 500, 1000, 4000, 8000]
    tiempos_fb = []
    tiempos_dyv = []
    repeticiones = 5
    semilla_fija = 42

    for n in tamanios:
        random.seed(semilla_fija)
        datos = [random.randint(-100, 100) for _ in range(n)]

        # Verificación de correctitud interna en cada tamaño
        s_fb = subarreglo_fuerza_bruta(datos)[2]
        s_dyv = subarreglo_maximo(datos, 0, n - 1)[2]
        assert s_fb == s_dyv, f"Error de consistencia matemática en tamaño n={n}"

        # Cronometrar únicamente la llamada a Fuerza Bruta
        inicio_fb = time.perf_counter()
        for _ in range(repeticiones):
            subarreglo_fuerza_bruta(datos)
        fin_fb = time.perf_counter()
        tiempo_prom_fb = ((fin_fb - inicio_fb) / repeticiones) * 1000

        # Cronometrar únicamente la llamada a Divide y Vencerás
        inicio_dyv = time.perf_counter()
        for _ in range(repeticiones):
            subarreglo_maximo(datos, 0, n - 1)
        fin_dyv = time.perf_counter()
        tiempo_prom_dyv = ((fin_dyv - inicio_dyv) / repeticiones) * 1000

        tiempos_fb.append(tiempo_prom_fb)
        tiempos_dyv.append(tiempo_prom_dyv)

    return tamanios, tiempos_fb, tiempos_dyv


def generar_grafica(tamanios: list[int], t_fb: list[float], t_dyv: list[float]) -> None:
    """Genera y guarda la gráfica comparativa de tiempo vs tamaño de entrada."""
    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(9, 6))
    plt.plot(tamanios, t_fb, marker='o', linestyle='-', color='crimson', label='Fuerza Bruta Θ(n²)')
    plt.plot(tamanios, t_dyv, marker='s', linestyle='-', color='dodgerblue', label='Divide y Vencerás Θ(n log n)')

    plt.title("Rendimiento Comparativo: Subarreglo Máximo")
    plt.xlabel("Tamaño de entrada n (número de registros / días)")
    plt.ylabel("Tiempo de ejecución promedio (milisegundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    ruta_imagen = os.path.join("graficas", "tiempo_vs_n.png")
    plt.savefig(ruta_imagen, dpi=300)
    plt.close()
    print(f"Gráfica guardada exitosamente en: {ruta_imagen}")


if __name__ == "__main__":
    print("Ejecutando experimentos y midiendo tiempos...")
    t, tfb, tdyv = medir_tiempos()
    generar_grafica(t, tfb, tdyv)