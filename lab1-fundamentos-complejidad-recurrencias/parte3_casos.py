"""Experimento de peor caso, mejor caso y caso promedio (Parte 3)."""

import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, mediana_de_tres
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": lambda n, semilla=42: generar_inverso(n),
}


def medir() -> dict[str, dict[str, list]]:
    """Mide tiempo y comparaciones de insertion sort en cada escenario.

    Cada tamano se mide REPETICIONES veces y se reporta la mediana
    del tiempo.

    Returns:
        Diccionario por escenario con las listas "tiempos" (segundos)
        y "comparaciones", una entrada por cada tamano de TAMANOS.
    """
    resultados = {nombre: {"tiempos": [], "comparaciones": []} for nombre in ESCENARIOS}
    for nombre, generador in ESCENARIOS.items():
        for n in TAMANOS:
            lote = generador(n)
            tiempos_rep = []
            comparaciones = None
            for _ in range(REPETICIONES):
                inicio = time.perf_counter()
                _, comparaciones = insertion_sort(lote)
                tiempos_rep.append(time.perf_counter() - inicio)
            resultados[nombre]["tiempos"].append(mediana_de_tres(*tiempos_rep))
            resultados[nombre]["comparaciones"].append(comparaciones)
    return resultados


def graficar(resultados: dict[str, dict[str, list]]) -> None:
    """Genera y guarda las graficas de comparaciones y de tiempo.

    Args:
        resultados: diccionario devuelto por medir().
    """
    plt.figure()
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["comparaciones"], marker="o", label=nombre)
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Numero de comparaciones")
    plt.title("Comparaciones de insertion sort segun escenario")
    plt.legend()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    plt.figure()
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["tiempos"], marker="o", label=nombre)
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.title("Tiempo de insertion sort segun escenario")
    plt.legend()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    graficar(medir())