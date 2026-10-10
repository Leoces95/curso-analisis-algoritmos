"""Script de pruebas unitarias para validar las soluciones del subarreglo máximo.

Sentido de orden declarado: Ascendente (de izquierda a derecha, índices de 0 a n-1).
"""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_pruebas() -> None:
    """Ejecuta todas las validaciones unitarias requeridas mediante assertions."""
    print("Iniciando pruebas unitarias...")

    # 1. Serie de ocho días de la situación problema (suma esperada: 17)
    serie_problema = [-3, 5, -2, 8, -6, 3, 9, -4]
    res_fb = subarreglo_fuerza_bruta(serie_problema)
    res_dyv = subarreglo_maximo(serie_problema, 0, len(serie_problema) - 1)
    assert res_fb[2] == 17, f"Falla fuerza bruta en caso problema: {res_fb[2]}"
    assert res_dyv[2] == 17, f"Falla divide y vencerás en caso problema: {res_dyv[2]}"

    # 2. Serie de un solo elemento
    serie_unitaria = [42]
    assert subarreglo_fuerza_bruta(serie_unitaria)[2] == 42
    assert subarreglo_maximo(serie_unitaria, 0, 0)[2] == 42

    # 3. Serie con todos los valores negativos
    serie_negativa = [-5, -2, -9, -1]
    assert subarreglo_fuerza_bruta(serie_negativa)[2] == -1
    assert subarreglo_maximo(serie_negativa, 0, len(serie_negativa) - 1)[2] == -1

    # 4. Serie con todos los valores positivos
    serie_positiva = [2, 4, 6, 8]
    assert subarreglo_fuerza_bruta(serie_positiva)[2] == 20
    assert subarreglo_maximo(serie_positiva, 0, len(serie_positiva) - 1)[2] == 20

    # 5. Caso donde el mejor tramo cruza explícitamente el punto medio
    serie_cruce = [-10, 15, 15, -10]
    assert subarreglo_fuerza_bruta(serie_cruce)[2] == 30
    assert subarreglo_maximo(serie_cruce, 0, len(serie_cruce) - 1)[2] == 30

    # 6. Al menos veinte listas aleatorias comparando ambas funciones
    random.seed(2026)
    for i in range(20):
        tamanio = random.randint(5, 40)
        lista_aleatoria = [random.randint(-100, 100) for _ in range(tamanio)]
        s_fb = subarreglo_fuerza_bruta(lista_aleatoria)[2]
        s_dyv = subarreglo_maximo(lista_aleatoria, 0, len(lista_aleatoria) - 1)[2]
        assert s_fb == s_dyv, (
            f"Discrepancia en lista aleatoria #{i+1} (tamaño {tamanio}): "
            f"Fuerza Bruta={s_fb}, Divide y Vencerás={s_dyv}"
        )

    print("¡Todas las pruebas unitarias pasaron exitosamente!")


if __name__ == "__main__":
    ejecutar_pruebas()