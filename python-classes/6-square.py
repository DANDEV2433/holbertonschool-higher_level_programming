#!/usr/bin/python3
"""
This module defines a Square class with a size with test Error
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a size and position

        Args:
            size (int): The size of the square.
            position (tuple): the position of the Square
                    TypeError  : if size isn't an integer
        """
        self.size = size
        self.position = position

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
        # Ajout de lignes vides en fonction de la position verticale
        for column in range(self.__position[1]):
            print("")
        # affichage du carré
        for row in range(self.__size):
            print(" " * self.__position[0] + '#' * self.__size)

    @property
    def position(self):
        """
        getter property for retrieve position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter property for set position

        TypeError:
                position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for num in value:
            if not isinstance(num, int) or num < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value
