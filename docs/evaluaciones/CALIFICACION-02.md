# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Leonel Antonio Martínez Silgado · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `f5dd95a`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 13 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 13 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (13 / 20)
**Lo que hizo bien:**
- En la pregunta 4 explica bien por qué dividir no ayuda para hallar el máximo: la recurrencia sale `T(n) = 2T(n/2) + O(1)`, es `Θ(n)` igual que un recorrido simple, y solo agrega llamadas recursivas.
- En la pregunta 5 recomienda divide y vencerás y declara que lo que da es una estimación.

**Lo que puede mejorar:**
- Pregunta 3: dice que divide y vencerás gana "desde n = 50", pero no muestra ningún dato medido que lo respalde; en su gráfica los tamaños pequeños quedan pegados al eje y no se distinguen. Debía apoyarse en una tabla con los tiempos medidos.
- Pregunta 5: no da una cifra para la fuerza bruta (solo "horas") ni para divide y vencerás (solo "una fracción de segundo o menos"). Con sus propios datos (unos 17 ms en n = 8000), `n log n` a un millón de registros da varios segundos, no una fracción de segundo. Debía hacer el cálculo con números.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica de dónde sale cada término y lo resuelve con el caso 2 del método maestro, verificando que `f(n) = Θ(n)`.
- Justifica el `Θ(n²)` de la fuerza bruta con los `n(n-1)/2` pares.

**Lo que puede mejorar:**
- Podría mostrar un poco más la verificación del caso (calcular `n^(log_2 2) = n` explícitamente).

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias; no modifican la lista y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- `pruebas.py` cubre todos los casos pedidos, con más de 20 listas aleatorias.
- Tiene type hints y docstrings estilo Google.

## 4. Calidad del análisis de las gráficas (13 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 7 tamaños.
- Midió con `perf_counter`, semilla fija, 5 repeticiones y verificó que ambas sumas coinciden.

**Lo que puede mejorar:**
- Pregunta 2: el informe dice que la fuerza bruta pasa de unos 630 ms a unos 2170 ms (factor 3.44), pero en la gráfica publicada la curva está cerca de 565 ms en n = 4000 y cerca de 2440 ms en n = 8000 (factor cercano a 4.3). Las cifras del informe no coinciden con su gráfica, y la explicación de "variaciones del sistema" no era necesaria: el factor real sí se acerca a 4.
- Para divide y vencerás no calculó el factor de crecimiento al duplicar `n` (solo dice que es "casi plano"), y no lo contrastó con lo que predice `Θ(n log n)` (algo más de 2).
- Las afirmaciones sobre tamaños pequeños no se apoyan en valores leídos.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab2-divide-y-vencer/` está en un lugar válido, con todos los archivos pedidos; el informe sigue el orden pedido, enlaza `subarreglo.py`, `pruebas.py` y `medicion.py`, y la gráfica se ve.
- Hay muchos commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones piden `pip install -r requirements.txt` desde la raíz y un `venv`, pero ese archivo no existe en la raíz del repositorio ni en la carpeta del laboratorio. Debe subirlo con `matplotlib` registrado.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas funciones dan resultados correctos y `medicion.py` corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Revise que cada cifra del informe coincida con lo que se lee en su gráfica publicada.
- Calcule el factor de crecimiento al duplicar `n` para todos los algoritmos, no solo para uno.
- Agregue una tabla de valores medidos para sustentar lo que dice de tamaños pequeños.
- Haga las estimaciones con números concretos y su razonamiento paso a paso.
- Registre las dependencias en `requirements.txt`.
