def calcular_promedio(lista: list[float]) -> float:
    """Calcula el promedio de los valores de una lista.

    Args:
        lista: Lista de números para calcular el promedio.

    Returns:
        El promedio de los valores de la lista.
    """
    suma = 0

    for numero in lista:
        suma = suma + numero

    return suma / len(lista)


def main() -> None:
    """Punto de entrada principal del programa."""
    lista = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(lista)

    print(f"El promedio es: {promedio}")


if __name__ == "__main__":
    main()