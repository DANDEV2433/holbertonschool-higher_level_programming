#!/usr/bin/python3
"""
function that returns the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    check the object is an instance of,
    or is an instance of a class that inherited from specidied class
    """
    return (isinstance(obj, a_class))
