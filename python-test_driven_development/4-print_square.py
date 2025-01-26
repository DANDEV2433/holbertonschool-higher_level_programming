#!/usr/bin/python3
"""
Module that prints a square with the character #.
"""


def print_square(size):
    """
prints a square with the character #.

Parameters:

    size: the size length of the square

    Returns: square with caracter #

    Raises:
    TypeError: size must be an integer
    ValueError: size must be >= 0

    """
    if size is None:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
