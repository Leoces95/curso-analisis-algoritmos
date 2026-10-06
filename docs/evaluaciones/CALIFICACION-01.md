# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Leonel Antonio Martínez Silgado · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `2610e45`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue entre que el resultado sea correcto y que llegue a tiempo, y nombra la ventana de 4 horas como la regla que se incumple.
- Explica que duplicar la velocidad no sirve porque el tiempo crece con el cuadrado de los datos.
- Aporta un segundo ejemplo propio (el proyecto del Runt) con cantidad de datos y límite de tiempo.
- En la parte ética identifica al paciente y al centro hospitalario como afectados y dice quién asume el costo.

**Lo que puede mejorar:**
- En el ejemplo del Runt falta cerrar bien la cuenta: con el doble de velocidad pasaría de 8–10 minutos a unos 5, pero el crecimiento de los datos no queda explicado.
- La parte ambiental es general: falta relacionar las horas de ejecución con el consumo de energía acumulado durante años.
- Se menciona que la lista debe ser precisa, pero falta desarrollar por qué el orden decide a quién se llama primero y qué obligación trae eso.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio indicando sobre qué se toma cada uno, y justifica que para la ventana estricta se usa el peor caso.
- Deja escrita la predicción antes del experimento.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve paso a paso con el método maestro, verificando la condición del caso 2.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- Dice que el escenario C llega "de menor a mayor" y que Tamiza ordena de mayor a menor, pero su código ordena de menor a mayor y su escenario C viene de mayor a menor. Hay que elegir un sentido, declararlo y mantenerlo en todo el informe.
- La tabla línea a línea de insertion sort no coincide exactamente con las líneas de su código (por ejemplo, el `if` y el `break`).

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista original y cuentan comparaciones entre elementos. No usan `sorted()` ni `sort()`.
- `merge_sort` tiene su propia mezcla recursiva.
- Los tres generadores dan listas del tamaño pedido, con valores distintos y semilla reproducible.

**Lo que puede mejorar:**
- Las funciones `ejecutar_experimento_p3` y `ejecutar_experimento_p4` no tienen docstring ni indicación del tipo que devuelven, y las funciones internas de `merge_sort` tampoco tienen docstring.
- Los archivos terminan sin salto de línea final (detalle de estilo PEP 8).
- Los algoritmos ordenan de menor a mayor, mientras que Tamiza necesita de mayor a menor; faltó declarar la decisión.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes con unidades y leyenda; las curvas van en los mismos ejes.
- Identifica correctamente el escenario C como peor caso, el B como mejor y el A como intermedio, con datos.
- Concluye que merge sort conviene, describiendo lo que hace cada curva, y lo relaciona con lo calculado.
- El concepto técnico recomienda merge sort, extrapola a 1.200.000 registros (insertion sort unas 11.7 horas) declarándolo como estimación, rechaza el servidor con una cifra y discute memoria y estabilidad.

**Lo que puede mejorar:**
- Dice que el escenario B es "lineal" y casi plano, pero en la gráfica el 2 % desordenado hace que sus comparaciones crezcan más de lo lineal.
- La explicación de por qué con tamaños pequeños las curvas se parecen es corta, y los tiempos citados de merge sort (0.008 s) no coinciden con lo que muestra la gráfica.
- En 4.3 conviene citar la gráfica de la que sale cada dato.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida y tiene todos los archivos pedidos.
- El informe está por partes, con las gráficas visibles, instrucciones de reproducción y su nombre.

**Lo que puede mejorar:**
- La Parte 3 no enlaza su código (`parte3_casos.py`, `algoritmos.py`, `datos.py`); solo la Parte 4 lo hace.
- Solo hay 2 commits que tocan este laboratorio (se pedían al menos 5 que muestren el avance).
- El informe incluye texto que no es parte de la respuesta (una frase de asistente antes de la Parte 3.1).

## ¿El código funciona?
Sí. Los scripts corren sin errores, ambos algoritmos ordenan correctamente y se generan las tres gráficas.

## Para el próximo laboratorio
- Elija un sentido de orden (mayor a menor o al revés), declárelo y manténgalo igual en generadores, algoritmos e informe.
- Agregue docstring y tipos a todas las funciones, incluidas las de los experimentos y las internas.
- Enlace el código en cada parte práctica desde el inicio de la parte.
- Haga commits pequeños y frecuentes mientras avanza (al menos cinco por laboratorio).
- Relacione cada cifra del concepto técnico con la gráfica de la que sale.
