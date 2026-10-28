import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ("en bodega", "en reparto", "entregado")

# Busqueda exitosa e infructuosa en la lista
lista = ListaEnlazada()
for guia, estado in ((1000000010, "en bodega"), (1000000024, "en reparto"),
                     (1000000017, "en bodega"), (1000000005, "entregado")):
    lista.insertar(guia, estado)
assert lista.tamano == 4
assert lista.cabeza is not None
assert lista.cabeza.guia == 1000000005  # se inserta al inicio
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000005) == "entregado"
assert lista.buscar(1000000099) is None
assert ListaEnlazada().buscar(1) is None

# Busqueda exitosa e infructuosa en la tabla
tabla = TablaHash(7)
for guia, estado in ((1000000010, "en bodega"), (1000000024, "en reparto"),
                     (1000000017, "en bodega"), (1000000005, "entregado")):
    tabla.insertar(guia, estado)
assert tabla.buscar(1000000024) == "en reparto"
assert tabla.buscar(1000000005) == "entregado"
assert tabla.buscar(1000000099) is None

# Colision forzada: con m = 7, 10, 24 y 17 caen en la casilla 3
tabla = TablaHash(7)
estados = {10: "en bodega", 24: "en reparto", 17: "entregado"}
for guia, estado in estados.items():
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, estado)
for guia, estado in estados.items():
    assert tabla.buscar(guia) == estado
assert tabla.buscar(99) is None
assert tabla.casillas[3].tamano == 3
assert all(tabla.casillas[i].tamano == 0 for i in range(7) if i != 3)
assert tabla.factor_carga() == 3 / 7

# Veinte colecciones aleatorias: lista y tabla deben coincidir
azar = random.Random(2026)
for ronda in range(20):
    n = azar.randint(1, 500)
    guias = azar.sample(range(10**9, 10**10), n)
    m = azar.choice((1, 7, 31, max(1, n // 2), n + 3))
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    esperado = {}
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
        esperado[guia] = estado
    assert tabla.factor_carga() == n / m
    for guia in guias:  # existentes
        assert lista.buscar(guia) == tabla.buscar(guia) == esperado[guia]
    conjunto = set(guias)
    for _ in range(100):  # inexistentes
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in conjunto:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

print("Todas las pruebas pasaron.")
