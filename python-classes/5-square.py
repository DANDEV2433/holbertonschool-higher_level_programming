#!/usr/bin/python3
"""
This module defines a Square class with a size with test Error
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes the square with a size 0

        Args:
            size (int): The size of the square.
            raise:  ValueError : if size is < O
                    TypeError  : if size isn't an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Utilise self pour définir l'attribut size

    def area(self):
        """
        returns the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        property getter for retrieve size

        Args:
            None
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
       property setter for set size

        Args:  Value of the size

        raise:  ValueError : if size is < O
                TypeError  : if size isn't an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                print("#" * self.__size)
