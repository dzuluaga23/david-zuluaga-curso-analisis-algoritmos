"""Comparacion de tiempo entre insertion sort y merge sort (Parte 4)."""

import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir():
    tiempos_insertion, tiempos_merge = [], []
    for n in TAMANOS:
        lote = generar_aleatorio(n)

        reps = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            insertion_sort(lote)
            reps.append(time.perf_counter() - inicio)
        tiempos_insertion.append(sorted(reps)[REPETICIONES // 2])

        reps = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            merge_sort(lote)
            reps.append(time.perf_counter() - inicio)
        tiempos_merge.append(sorted(reps)[REPETICIONES // 2])

    return tiempos_insertion, tiempos_merge


def graficar(tiempos_insertion, tiempos_merge):
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