#!/usr/bin/python3
"""
empty class BaseGeometry
"""


class BaseGeometry:
    """
    empty class
    """

    def area(self):
        """
        public instance method with raise exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method that validate value
        if the value is not an integer: TypeError or ValueError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
