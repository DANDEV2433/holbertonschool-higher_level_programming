#!/usr/bin/python3
"""
initialize class Rectangle with your width and height with
integer_validator method and pass to private
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        check attribut with integer_validator and pass to private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        print area of the rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        instantiation with size
        """
        self.integer_validator("size", size)
        """
        use super() for call the constructor of the
        immediate parent class (Rectangle).
        Rectangle constructor takes width and height as arguments,
        size is passed for both.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        return rectangle description
        """
        return f"[Square] {self.__size}/{self.__size}"
