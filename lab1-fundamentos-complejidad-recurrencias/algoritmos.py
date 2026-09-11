"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if lista[j] < actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = actual
    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    def _mezclar_ordenar(lista: list[int]) -> tuple[list[int], int]:
        if len(lista) <= 1:
            return lista, 0
        medio = len(lista) // 2
        izq, comp_izq = _mezclar_ordenar(lista[:medio])
        der, comp_der = _mezclar_ordenar(lista[medio:])
        resultado = []
        i = j = 0
        comparaciones = comp_izq + comp_der
        while i < len(izq) and j < len(der):
            comparaciones += 1
            if izq[i] >= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado, comparaciones

    return _mezclar_ordenar(datos.copy())