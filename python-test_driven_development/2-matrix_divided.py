#!/usr/bin/python3
"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
Divides all elements of a matrix by a divisor

Parameters:

    matrix: a list of lists of numbers: integers or floats
    div: int or float divisor

    Returns:
    the new matrix with the result of dividing the numbers in the lists

    Raises:
    TypeError: If matrix is not a list or if element is not integers or floats.
    ZeroDivisionEroor: if div is 0.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    # Vérifier que matrix est une liste de listes
    if not isinstance(matrix, list):
        raise TypeError(
            "error"
        )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "error"
        )
    # Vérifier que chaque élément de matrix est un nombre
    for row in matrix:
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError(
                    "error"
                )
    # Vérifier que toutes les lignes de matrix ont la même taille
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size")
    # Vérifier que div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # création d'une nouvelle matrix avec les résulatat de la div
    new_matrix = []
    for row in matrix:
        new_row = []
        for number in row:
            new_row.append(round(number / div, 2))
        new_matrix.append(new_row)
    return new_matrix
