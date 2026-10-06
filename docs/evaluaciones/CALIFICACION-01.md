# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** David Zuluaga Ceballos · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `126efdd`

Muy buen trabajo: un informe completo, con datos propios y código que funciona.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Explica que Tamiza ordena bien pero no a tiempo, y nombra la restricción que incumple: la ventana de cuatro horas.
- Explica que duplicar el servidor ayuda poco porque insertion sort crece de forma cuadrática.
- Da un ejemplo propio (la sesión de asesoría de matrícula con 26 mil estudiantes) y aclara con honestidad que no sabe qué algoritmo usaba.
- Relaciona el funcionamiento durante años con el gasto de energía.
- Señala perjuicios concretos (el paciente y el operador del centro) y dice quién asume el costo.
- Explica por qué el orden de la lista, que decide a quién se llama primero, obliga a que el ordenamiento sea siempre correcto.

**Lo que puede mejorar:**
- En el ejemplo propio falta decir con más claridad qué límite se incumplía (por ejemplo, cuánto tardaba cada petición frente a cuánto debía tardar).
- La relación entre tiempo de ejecución y energía puede apoyarse en una idea más concreta, como las horas extra de servidor encendido cada noche.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio indicando sobre qué conjunto de entradas se toma el máximo, el mínimo y el promedio.
- Justifica que usaría el peor caso para decidir la entrada a producción y deja escrita su predicción antes del experimento.
- La recurrencia de merge sort está bien explicada y resuelta con el método maestro, verificando el caso 2.
- El análisis línea por línea de insertion sort cubre peor caso, mejor caso y caso promedio, y la tabla de complejidades es correcta.

**Lo que puede mejorar:**
- La predicción usa un ejemplo con n = 5; sería más claro enunciarla para un tamaño general o grande y dejarla separada del resto de la explicación.
- En el análisis línea por línea, indique el costo de cada línea con su propia constante en una tabla, para que la suma se vea más fácil.

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista recibida y cuentan comparaciones entre elementos.
- `merge_sort` tiene su propia mezcla recursiva y no usa funciones de ordenamiento.
- Los generadores producen lotes correctos, con índices distintos y semilla reproducible.
- Todas las funciones tienen *type hints* y *docstrings*.

**Lo que puede mejorar:**
- Hay un detalle de estilo (PEP 8): un espacio de más antes de los dos puntos en una variable de `merge_sort`.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados con unidades y leyenda, y las curvas están en los mismos ejes.
- Identifica bien el peor caso (C), el mejor (B) y el promedio (A), y explica por qué la gráfica de tiempo se parece a la de comparaciones. Indica que midió tres veces y usó la mediana.
- Concluye que merge sort conviene y lo contrasta con las complejidades calculadas.
- En 4.3 recomienda merge sort, estima el tiempo para 1.200.000 registros declarándolo como estimación, responde a la propuesta del servidor con un dato medido y discute memoria y estabilidad.

**Lo que puede mejorar:**
- Para tamaños pequeños, explique por qué merge sort puede no ganar todavía: crear listas nuevas y llamar funciones recursivas también cuesta.
- Al mencionar que las curvas se separan cerca de n = 1000, apóyese en un valor medido concreto de la gráfica.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos coinciden con lo pedido, las gráficas se ven en el informe y cada parte enlaza su código.
- Las instrucciones de reproducción están completas.
- Hay ocho commits sobre el laboratorio, con mensajes descriptivos.

## ¿El código funciona?
Sí. Los scripts corren sin errores y generan las tres gráficas. Los dos algoritmos ordenan bien los tres escenarios.

## Para el próximo laboratorio
- Cuando dé un ejemplo propio, diga qué se procesa, cuántos datos hay y qué límite exacto se incumple.
- Escriba las predicciones de forma separada y para un tamaño general, antes de mostrar resultados.
- Explique también los resultados que parecen raros con tamaños pequeños.
- Revise el estilo del código (PEP 8) antes de entregar.
