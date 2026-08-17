"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.
"""
import statistics


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).

    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese años separados por comas (ej. 2000,2023,2024): ")
        partes = entrada.split(",")
        try:
            anios = [int(parte.strip()) for parte in partes]
            for anio in anios:
                if anio < 0:
                    raise ValueError("Los años no pueden ser números negativos.")
            return anios
        except ValueError:  
            print(f"Error: No ingresó años válidos, recuerde separar por coma cada año. Intente de nuevo.\n")


def main() -> None:
    """Punto de entrada del script."""
    anios = leer_anios()
    bisiestos = [anio for anio in anios if es_bisiesto(anio)]

    print(f"\nAños ingresados: {anios}")
    print(f"Años bisiestos: {bisiestos}")
    print(f"Cantidad de años bisiestos: {len(bisiestos)} de {len(anios)}")

    decadas_unicas = { (anio // 10) * 10 for anio in anios }
    anios_por_decada = {
        decada: [anio for anio in anios if (anio // 10) * 10 == decada]
        for decada in sorted(decadas_unicas)
    }
    print(f"Años agrupados por década: {anios_por_decada}")

    if bisiestos:
        promedio_bisiestos = statistics.mean(bisiestos)
        print(f"Promedio de años bisiestos: {promedio_bisiestos:.2f}")
    else:
        print("Promedio de años bisiestos: N/A (no se ingresaron años bisiestos)")


if __name__ == "__main__":
    main()