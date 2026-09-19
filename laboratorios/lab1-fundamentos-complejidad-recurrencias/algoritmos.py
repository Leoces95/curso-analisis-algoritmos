"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia = list(datos)
    comparaciones = 0
    n = len(copia)

    for i in range(1, n):
        clave = copia[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if copia[j] > clave:
                copia[j + 1] = copia[j]
                j -= 1
            else:
                break
        copia[j + 1] = clave

    return copia, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia = list(datos)

    def _merge_sort_rec(arr: list[int]) -> tuple[list[int], int]:
        if len(arr) <= 1:
            return arr, 0

        medio = len(arr) // 2
        izquierda, comps_izq = _merge_sort_rec(arr[:medio])
        derecha, comps_der = _merge_sort_rec(arr[medio:])

        mezclada, comps_mezcla = _mezclar(izquierda, derecha)
        total_comps = comps_izq + comps_der + comps_mezcla

        return mezclada, total_comps

    def _mezclar(izq: list[int], der: list[int]) -> tuple[list[int], int]:
        resultado = []
        i = j = 0
        comparaciones = 0

        while i < len(izq) and j < len(der):
            comparaciones += 1
            if izq[i] <= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1

        resultado.extend(izq[i:])
        resultado.extend(der[j:])

        return resultado, comparaciones

    return _merge_sort_rec(copia)