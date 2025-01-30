#!/usr/bin/python3
"""
This module defines a rectangle with your width and your height
"""


class Rectangle:
    """
    class that defines a Rectangle with your arguments.
    Attribut class for count instances
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a width and height

        Args:
            width (int): The width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        method that returns the biggest rectangle based on the area
        raises:
                TypeError("rect_1 must be an instance of Rectangle")
                TypeError("rect_2 must be an instance of Rectangle")
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        method class for new instance of Rectangle width == height == size
        """
        return cls(width=size, height=size)
