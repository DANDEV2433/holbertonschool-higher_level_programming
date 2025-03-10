#!/usr/bin/python3
"""
Module for adding two integers.
"""


def add_integer(a, b=98):
    """
Adds two integers or floats and returns an integer.

Parameters:
    a (int, float): The first number to be added. Must be an integer or float.
    b (int, float): The second number to be added. Must be an integer or float.
    Returns:
    int: The sum of a and b, casted to an integer.
    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")
    if (a != a):
        raise TypeError("a must be a valid number")
    if (b != b):
        raise TypeError("b must be a valid number")
    return int(a) + int(b)
