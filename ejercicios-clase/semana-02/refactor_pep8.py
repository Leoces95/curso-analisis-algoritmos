def calcular_promedio(lista_numeros: list[float]) -> float:
    """Calcula el promedio aritmético de una lista de números.

    Args:
        lista_numeros: Lista de enteros o flotantes a promediar.

    Returns:
        El promedio aritmético como un número de punto flotante.
    """
    suma_total = 0.0
    for numero in lista_numeros:
        suma_total += numero
    return suma_total / len(lista_numeros)


def main() -> None:
    """Punto de entrada principal del script."""
    numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(numeros)
    print(promedio)


if __name__ == "__main__":
    main()