# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** David Zuluaga Ceballos · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `52cae52`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 16 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **74 / 100** |
| **Nota (0–5)** | **3.70** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Explica que Tamiza ordena bien pero no a tiempo, y que duplicar el servidor ayuda poco porque insertion sort crece de forma cuadrática.
- Relaciona el funcionamiento durante años con el gasto de energía.
- Identifica perjuicios concretos (el paciente y el operador del centro) y dice quién asume el costo.

**Lo que puede mejorar:**
- Nombre con claridad la restricción incumplida: la ventana de cuatro horas.
- Su ejemplo propio (el sistema de matrículas) no dice qué algoritmo falló, cuántos datos se procesaban ni qué límite se incumplía. Falta concretarlo.
- Falta desarrollar mejor por qué el orden de la lista, que decide a quién se llama primero, obliga a que el ordenamiento sea siempre correcto.

## 2. Calidad de la explicación teórica (16 / 25)
**Lo que hizo bien:**
- La recurrencia de merge sort está bien explicada y resuelta con el método maestro, verificando que se cumple el caso 2.
- El análisis de insertion sort por líneas y la tabla de complejidades están presentes y son correctos.
- Justifica que usaría el peor caso para decidir la entrada a producción, y su predicción sobre los escenarios coincidió con lo medido.

**Lo que puede mejorar:**
- En la Parte 3.1 no define peor caso, mejor caso y caso promedio indicando sobre qué conjunto de entradas se toma el máximo, el mínimo o el promedio. Usar "n = 5" como ejemplo no basta.
- La predicción mezcla la explicación con razonamientos confusos; debe quedar escrita de forma clara y separada antes del experimento.
- En el análisis línea por línea faltan los costos del mejor caso y el caso promedio de insertion sort, y la suma total de todas las líneas.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida y cuentan comparaciones entre elementos.
- `merge_sort` tiene su propia mezcla recursiva y no usa funciones de ordenamiento.
- Los generadores producen lotes correctos y con semilla reproducible.

**Lo que puede mejorar:**
- Las funciones `medir`, `graficar` y la función interna de `merge_sort` no tienen *type hints* ni *docstring*.
- Los archivos terminan sin salto de línea final (PEP 8).
- En los scripts de medición se usa `sorted()` para sacar la mediana; es mejor evitarlo.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes, unidades y leyenda, y las curvas están en los mismos ejes.
- Identifica bien el peor caso (C), el mejor (B) y el promedio (A), y la gráfica de la Parte 4 muestra claramente la diferencia entre ambos algoritmos.
- En 4.3 recomienda merge sort, extrapola a 1.200.000 registros declarándolo como estimación y responde a la propuesta del servidor con un dato medido.

**Lo que puede mejorar:**
- En 4.3 falta una consideración distinta del tiempo, como la memoria extra de merge sort o la estabilidad.
- Algunas frases no se ven en las gráficas, por ejemplo el punto exacto donde las curvas se separan.
- No explica por qué la gráfica de tiempo se parece a la de comparaciones. No indica que midió tres veces y usó la mediana.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos coinciden con lo pedido, las gráficas se ven en el informe y cada parte enlaza su código.
- Hay varios commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de la Parte 4 dicen "cuando esté lista"; deben quedar definitivas.

## ¿El código funciona?
Sí. Los scripts corren sin errores y generan las tres gráficas. Los dos algoritmos ordenan bien los tres escenarios.

## Para el próximo laboratorio
- Defina cada concepto teórico indicando exactamente sobre qué se calcula.
- Cuando dé un ejemplo propio, diga qué se procesa, cuántos datos hay y qué límite se incumple.
- Agregue *type hints* y *docstrings* a todas las funciones, también a las de apoyo.
- Revise que cada parte pedida (por ejemplo, la consideración adicional de 4.3) esté completa antes de entregar.
