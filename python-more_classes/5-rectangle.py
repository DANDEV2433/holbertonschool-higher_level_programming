#!/usr/bin/python3
"""
This module defines a rectangle with your width and your height
"""


class Rectangle:
    """
    class that defines a Rectangle with your arguments.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a width and height

        Args:
            width (int): The width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter method to retrieve the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for setting the value of the width

        raises:
                TypeError("width must be an integer")
                ValueError("width must be >= 0")
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method to retrieve the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for setting the value of the height

        raises:
                TypeError("height must be an integer")
                ValueError("message height must be >= 0")
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        print the rectangle with the character "#"
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            # Ajoute une ligne de caractères '#' suivie d'un saut de ligne
            rectangle_str += "#" * self.__width + "\n"
            # Supprime le dernier saut de ligne, éviter une ligne vide en plus
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        method for a string representation of the rectangle
        so that a new instance can be recreated using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        print a message when the rectangle instance is deleted
        """
        print("Bye rectangle...")
