"""Subarreglo máximo: fuerza bruta y divide y vencerás. """


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Calcula el subarreglo de mayor suma evaluando todas las parejas de índices (i, j).

    Args:
        valores: Secuencia numérica con las variaciones de caja. No se modifica.

    Returns:
        Una tupla (indice_inicio, indice_fin, suma_maxima) correspondiente al tramo.
    """
    total_elementos = len(valores)
    idx_inicio = 0
    idx_fin = 0
    suma_max = valores[0]

    for i in range(total_elementos):
        suma_parcial = 0.0
        for j in range(i, total_elementos):
            suma_parcial += valores[j]
            if suma_parcial > suma_max:
                suma_max = suma_parcial
                idx_inicio = i
                idx_fin = j

    return (idx_inicio, idx_fin, suma_max)


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Determina el tramo máximo que atraviesa el punto medio del subarreglo.

    Args:
        valores: Secuencia numérica original. No se modifica.
        inicio: Límite izquierdo del rango actual (inclusive).
        medio: Índice central que divide las dos mitades.
        fin: Límite derecho del rango actual (inclusive).

    Returns:
        Una tupla (indice_inicio, indice_fin, suma_cruzada) con el mejor cruce.
    """
    # Barrido hacia la izquierda desde el punto medio
    max_izq = -float("inf")
    acumulado_izq = 0.0
    mejor_i = medio

    for i in range(medio, inicio - 1, -1):
        acumulado_izq += valores[i]
        if acumulado_izq > max_izq:
            max_izq = acumulado_izq
            mejor_i = i

    # Barrido hacia la derecha desde el punto medio + 1
    max_der = -float("inf")
    acumulado_der = 0.0
    mejor_j = medio + 1

    for j in range(medio + 1, fin + 1):
        acumulado_der += valores[j]
        if acumulado_der > max_der:
            max_der = acumulado_der
            mejor_j = j

    return (mejor_i, mejor_j, max_izq + max_der)


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra recursivamente el subarreglo de mayor suma usando divide y vencerás.

    Args:
        valores: Secuencia numérica original. No se modifica.
        inicio: Índice inicial del subsegmento (inclusive).
        fin: Índice final del subsegmento (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) con los datos del mejor tramo.
    """
    # Caso base: un único elemento en el rango
    if inicio == fin:
        return (inicio, fin, valores[inicio])

    medio = (inicio + fin) // 2  # <--- Corregido: división entera entre 2

    # Conquistar y dividir: llamadas recursivas y caso cruzado
    i_izq, f_izq, s_izq = subarreglo_maximo(valores, inicio, medio)
    i_der, f_der, s_der = subarreglo_maximo(valores, medio + 1, fin)
    i_cruz, f_cruz, s_cruz = suma_cruzada(valores, inicio, medio, fin)

    # Combinar: retornar el mejor de los tres casos evaluados
    if s_izq >= s_der and s_izq >= s_cruz:
        return (i_izq, f_izq, s_izq)
    elif s_der >= s_izq and s_der >= s_cruz:
        return (i_der, f_der, s_der)
    else:
        return (i_cruz, f_cruz, s_cruz)