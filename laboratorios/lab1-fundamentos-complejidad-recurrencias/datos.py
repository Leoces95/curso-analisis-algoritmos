"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    return rng.sample(range(0, max(1001, n * 10)), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos.
    """
    rng = random.Random(semilla)
    datos_base = rng.sample(range(0, max(1001, n * 10)), n)

    n_ordenado = int(n * 0.98)
    # Ordenamos de forma ascendente el 98% para que sea el mejor caso teorico progresivo
    parte_ordenada = list(datos_base[:n_ordenado])
    # Implementacion manual de insertion sort simple solo para preparar el escenario sin librerias
    for i in range(1, len(parte_ordenada)):
        k = parte_ordenada[i]
        j = i - 1
        while j >= 0 and parte_ordenada[j] > k:
            parte_ordenada[j + 1] = parte_ordenada[j]
            j -= 1
        parte_ordenada[j + 1] = k

    parte_desordenada = datos_base[n_ordenado:]
    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en orden descendente.
    """
    return list(range(n, 0, -1))