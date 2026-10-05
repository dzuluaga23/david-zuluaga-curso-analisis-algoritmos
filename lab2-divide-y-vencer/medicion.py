"""Medicion del tiempo de fuerza bruta vs divide y venceras."""

import random
import statistics
import time
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 5
SEMILLA = 42
RUTA_GRAFICA = Path(__file__).parent / "graficas" / "tiempo_vs_n.png"


def generar_datos(n: int, semilla: int) -> list[int]:
    """Genera una serie reproducible de n enteros entre -100 y 100.

    Args:
        n: cantidad de dias (tamano de la entrada).
        semilla: semilla fija del generador aleatorio.

    Returns:
        Lista de n enteros aleatorios en el rango [-100, 100].
    """
    generador = random.Random(semilla)
    return [generador.randint(-100, 100) for _ in range(n)]


def medir(
    algoritmo: Callable[[], tuple[int, int, float]], repeticiones: int
) -> tuple[float, float]:
    """Cronometra solo la llamada al algoritmo y devuelve la mediana.

    Args:
        algoritmo: funcion sin argumentos que ejecuta el algoritmo.
        repeticiones: cuantas veces se repite la medicion.

    Returns:
        Una tupla (mediana del tiempo en milisegundos, suma obtenida).
    """
    tiempos: list[float] = []
    resultado = (0, 0, 0.0)
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        resultado = algoritmo()
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)
    return statistics.median(tiempos), resultado[2]


def ejecutar_experimento() -> tuple[list[float], list[float]]:
    """Mide ambos algoritmos en cada tamano y verifica que coincidan.

    Returns:
        Dos listas con los tiempos en ms: (fuerza bruta, divide y venceras).
    """
    tiempos_bruta: list[float] = []
    tiempos_dyv: list[float] = []
    print(f"{'n':>6} {'bruta (ms)':>12} {'d y v (ms)':>12}")

    for n in TAMANOS:
        serie = generar_datos(n, SEMILLA)  # fuera del cronometro
        t_bruta, suma_bruta = medir(
            lambda: subarreglo_fuerza_bruta(serie), REPETICIONES
        )
        t_dyv, suma_dyv = medir(
            lambda: subarreglo_maximo(serie, 0, n - 1), REPETICIONES
        )
        assert suma_bruta == suma_dyv, f"Sumas distintas con n={n}"
        tiempos_bruta.append(t_bruta)
        tiempos_dyv.append(t_dyv)
        print(f"{n:>6} {t_bruta:>12.4f} {t_dyv:>12.4f}")

    return tiempos_bruta, tiempos_dyv


def graficar(
    tamanos: list[int], tiempos_bruta: list[float], tiempos_dyv: list[float]
) -> None:
    """Dibuja ambas curvas en los mismos ejes y guarda el PNG.

    Args:
        tamanos: tamanos de entrada medidos.
        tiempos_bruta: tiempos (ms) de la fuerza bruta.
        tiempos_dyv: tiempos (ms) de divide y venceras.
    """
    RUTA_GRAFICA.parent.mkdir(exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos_bruta, marker="o", label="Fuerza bruta")
    plt.plot(tamanos, tiempos_dyv, marker="s", label="Divide y venceras")
    plt.title("Tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada n (numero de dias)")
    plt.ylabel("Tiempo de ejecucion (milisegundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig(RUTA_GRAFICA, dpi=150, bbox_inches="tight")


def main() -> None:
    """Ejecuta el experimento completo y genera la grafica."""
    tiempos_bruta, tiempos_dyv = ejecutar_experimento()
    graficar(TAMANOS, tiempos_bruta, tiempos_dyv)
    print(f"Grafica guardada en {RUTA_GRAFICA}")


if __name__ == "__main__":
    main()