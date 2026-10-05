"""Comparacion de tiempo entre insertion sort y merge sort (Parte 4)."""

import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, mediana_de_tres, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir() -> tuple[list[float], list[float]]:
    """Mide el tiempo de insertion sort y merge sort en el escenario A.

    Cada tamano se mide REPETICIONES veces y se reporta la mediana.

    Returns:
        Una tupla con la lista de tiempos (segundos) de insertion sort
        y la de merge sort, una entrada por cada tamano de TAMANOS.
    """
    tiempos_insertion, tiempos_merge = [], []
    for n in TAMANOS:
        lote = generar_aleatorio(n)

        reps = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            insertion_sort(lote)
            reps.append(time.perf_counter() - inicio)
        tiempos_insertion.append(mediana_de_tres(*reps))

        reps = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            merge_sort(lote)
            reps.append(time.perf_counter() - inicio)
        tiempos_merge.append(mediana_de_tres(*reps))

    return tiempos_insertion, tiempos_merge


def graficar(tiempos_insertion: list[float], tiempos_merge: list[float]) -> None:
    """Genera y guarda la grafica de tiempo de ambos algoritmos.

    Args:
        tiempos_insertion: tiempos de insertion sort por tamano.
        tiempos_merge: tiempos de merge sort por tamano.
    """
    plt.figure()
    plt.plot(TAMANOS, tiempos_insertion, marker="o", label="Insertion sort")
    plt.plot(TAMANOS, tiempos_merge, marker="o", label="Merge sort")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.title("Insertion sort vs merge sort (escenario A)")
    plt.legend()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ti, tm = medir()
    graficar(ti, tm)