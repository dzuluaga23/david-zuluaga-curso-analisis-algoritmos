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
        """Divide la lista en dos mitades, las ordena y las mezcla.

        En un empate toma primero el elemento de la izquierda, lo que
        hace al algoritmo estable.

        Args:
            lista: sublista de indices de riesgo a ordenar.

        Returns:
            Una tupla con la sublista ordenada de mayor a menor y el
            numero de comparaciones realizadas.
        """
        if len(lista) <= 1:
            return lista, 0
        medio = len(lista) // 2
        izq, comp_izq = _mezclar_ordenar(lista[:medio])
        der, comp_der = _mezclar_ordenar(lista[medio:])
        resultado : list[int] = []
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


def mediana_de_tres(a: float, b: float, c: float) -> float:
    """Devuelve la mediana de tres valores sin usar funciones de ordenamiento.

    Args:
        a: primer valor.
        b: segundo valor.
        c: tercer valor.

    Returns:
        El valor que queda en medio al quitar el minimo y el maximo.
    """
    return a + b + c - min(a, b, c) - max(a, b, c)