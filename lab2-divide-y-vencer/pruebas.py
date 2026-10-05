import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ambas(serie: list[float]) -> tuple[float, float]:
    """Devuelve la suma de cada algoritmo sobre la misma serie."""
    return (
        subarreglo_fuerza_bruta(serie)[2],
        subarreglo_maximo(serie, 0, len(serie) - 1)[2],
    )


assert ambas([-3, 5, -2, 8, -6, 3, 9, -4]) == (17, 17)

assert ambas([7]) == (7, 7)
assert ambas([-7]) == (-7, -7)

assert ambas([-8, -3, -5, -1, -9]) == (-1, -1)

assert ambas([2, 4, 1, 3]) == (10, 10)

cruzado = [-2, 4, 3, -1, 6, -5]
assert ambas(cruzado) == (12, 12)
assert subarreglo_maximo(cruzado, 0, 5)[:2] == (1, 4)

copia = cruzado.copy()
subarreglo_maximo(cruzado, 0, 5)
subarreglo_fuerza_bruta(cruzado)
assert cruzado == copia

random.seed(42)
for _ in range(30):
    n = random.randint(1, 60)
    serie = [random.randint(-100, 100) for _ in range(n)]
    bruta, dyv = ambas(serie)
    assert bruta == dyv
    i, j, s = subarreglo_maximo(serie, 0, n - 1)
    assert sum(serie[i : j + 1]) == s  

print("Todas las pruebas pasaron")