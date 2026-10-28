"""Experimentos de tiempo de busqueda: lista enlazada frente a tabla hash."""

import gc
import os
import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

SEMILLA = 42
BUSQUEDAS = 200
REPETICIONES = 15
TAMANOS = [100, 500, 1000, 5000, 20000, 50000, 100000]
N_FIJO = 20000
ALFAS = [0.25, 0.5, 1, 2, 4, 10]
ESTADOS = ("en bodega", "en reparto", "entregado")
CARPETA = os.path.dirname(os.path.abspath(__file__))


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(k: int) -> bool:
    """Indica si un entero es primo.

    Args:
        k: entero a revisar.

    Returns:
        True si k es primo.
    """
    if k < 2:
        return False
    divisor = 2
    while divisor * divisor <= k:
        if k % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor.

    Args:
        objetivo: valor de referencia.

    Returns:
        El primo mas cercano a objetivo (el menor si hay empate).
    """
    distancia = 0
    while True:
        if es_primo(objetivo - distancia):
            return objetivo - distancia
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        distancia += 1


def construir(
    n: int, m: int, semilla: int = SEMILLA
) -> tuple[ListaEnlazada, TablaHash, list[int]]:
    """Construye una lista y una tabla con las mismas n guias.

    Args:
        n: numero de guias.
        m: numero de casillas de la tabla.
        semilla: semilla del generador de guias.

    Returns:
        La lista, la tabla y las guias insertadas.
    """
    azar = random.Random(semilla)
    guias = azar.sample(range(10**9, 10**10), n)
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla, guias


def verificar(lista: ListaEnlazada, tabla: TablaHash, guias: list[int]) -> None:
    """Comprueba que lista y tabla dan el mismo estado en una muestra.

    Args:
        lista: lista enlazada con las guias.
        tabla: tabla hash con las mismas guias.
        guias: guias existentes.
    """
    muestra = random.Random(SEMILLA).sample(guias, min(200, len(guias)))
    for guia in muestra:
        estado = lista.buscar(guia)
        assert estado is not None and estado == tabla.buscar(guia)


def tiempo_medio_us(estructura: ListaEnlazada | TablaHash, claves: list[int]) -> float:
    """Mide el tiempo medio de busqueda, solo cronometrando las busquedas.

    Args:
        estructura: lista o tabla donde buscar.
        claves: guias a buscar.

    Returns:
        Tiempo medio por busqueda en microsegundos: la menor de las
        medias de REPETICIONES repeticiones, para descartar el ruido
        del sistema operativo.
    """
    gc.collect()
    gc.disable()
    medias = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in claves:
            estructura.buscar(guia)
        medias.append((time.perf_counter() - inicio) / len(claves))
    gc.enable()
    return min(medias) * 1e6


def experimento_a() -> tuple[list[int], list[int], list[float], list[float]]:
    """Mide lista y tabla para distintos n con alfa cercano a 2.

    Returns:
        Los n, los m usados, y los tiempos medios (us) de lista y tabla.
    """
    ms, t_lista, t_tabla = [], [], []
    for n in TAMANOS:
        m = primo_cercano(n // 2)
        lista, tabla, guias = construir(n, m)
        verificar(lista, tabla, guias)
        claves = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        ms.append(m)
        t_lista.append(tiempo_medio_us(lista, claves))
        t_tabla.append(tiempo_medio_us(tabla, claves))
    return TAMANOS, ms, t_lista, t_tabla


def experimento_b() -> tuple[list[int], list[float], list[float]]:
    """Mide la tabla con n fijo y distintos factores de carga.

    Returns:
        Los m usados, los alfa reales y los tiempos medios (us).
    """
    ms, alfas, tiempos = [], [], []
    for alfa in ALFAS:
        m = primo_cercano(round(N_FIJO / alfa))
        lista, tabla, guias = construir(N_FIJO, m)
        verificar(lista, tabla, guias)
        claves = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        ms.append(m)
        alfas.append(tabla.factor_carga())
        tiempos.append(tiempo_medio_us(tabla, claves))
    return ms, alfas, tiempos


def graficar_a(
    ns: list[int], t_lista: list[float], t_tabla: list[float], log: bool
) -> None:
    """Grafica tiempo medio frente a n y la guarda como PNG.

    Args:
        ns: numeros de guias.
        t_lista: tiempos de la lista (us).
        t_tabla: tiempos de la tabla (us).
        log: si es True, usa ejes logaritmicos y otro archivo.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(ns, t_lista, "o-", label="Lista enlazada")
    plt.plot(ns, t_tabla, "s-", label="Tabla hash (alfa ≈ 2)")
    if log:
        plt.xscale("log")
        plt.yscale("log")
    plt.title("Busqueda de guias inexistentes: lista vs tabla"
              + (" (escala log)" if log else ""))
    plt.xlabel("Numero de guias n (unidades)")
    plt.ylabel("Tiempo medio por busqueda (µs)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    nombre = "lista_vs_tabla_log.png" if log else "lista_vs_tabla.png"
    plt.savefig(os.path.join(CARPETA, "graficas", nombre), dpi=150,
                bbox_inches="tight")
    plt.close()


def graficar_b(alfas: list[float], tiempos: list[float]) -> None:
    """Grafica tiempo medio frente a alfa y la guarda como PNG.

    Args:
        alfas: factores de carga.
        tiempos: tiempos de la tabla (us).
    """
    plt.figure(figsize=(8, 5))
    plt.plot(alfas, tiempos, "o-", label=f"Tabla hash (n = {N_FIJO})")
    plt.title("Efecto del factor de carga en la busqueda")
    plt.xlabel("Factor de carga α = n / m (adimensional)")
    plt.ylabel("Tiempo medio por busqueda (µs)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(CARPETA, "graficas", "tiempo_vs_alfa.png"),
                dpi=150, bbox_inches="tight")
    plt.close()


def imprimir_factores(nombre: str, xs: list[float], ts: list[float]) -> None:
    """Imprime el factor de crecimiento entre valores consecutivos.

    Args:
        nombre: nombre de la serie.
        xs: valores del eje x.
        ts: tiempos medidos.
    """
    print(f"\nFactores de crecimiento - {nombre}")
    for i in range(1, len(xs)):
        print(f"  {xs[i - 1]} -> {xs[i]}: x{xs[i] / xs[i - 1]:.2f} en tamano, "
              f"tiempo x{ts[i] / ts[i - 1]:.2f}")


def main() -> None:
    """Ejecuta ambos experimentos, imprime tablas y guarda las graficas."""
    os.makedirs(os.path.join(CARPETA, "graficas"), exist_ok=True)

    ns, ms, t_lista, t_tabla = experimento_a()
    print("Experimento A: busquedas de guias inexistentes")
    print("| n | m | alfa | lista (us) | tabla (us) |")
    for n, m, tl, tt in zip(ns, ms, t_lista, t_tabla):
        print(f"| {n} | {m} | {n / m:.2f} | {tl:.2f} | {tt:.3f} |")
    imprimir_factores("lista", ns, t_lista)
    imprimir_factores("tabla", ns, t_tabla)
    graficar_a(ns, t_lista, t_tabla, log=False)
    graficar_a(ns, t_lista, t_tabla, log=True)

    ms_b, alfas, tiempos = experimento_b()
    print(f"\nExperimento B: n = {N_FIJO}")
    print("| m | alfa | tabla (us) |")
    for m, a, t in zip(ms_b, alfas, tiempos):
        print(f"| {m} | {a:.2f} | {t:.3f} |")
    imprimir_factores("tabla vs alfa", alfas, tiempos)
    graficar_b(alfas, tiempos)


if __name__ == "__main__":
    main()
