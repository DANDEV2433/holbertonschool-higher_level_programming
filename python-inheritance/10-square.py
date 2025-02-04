#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


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

    def area(self):
        """
        print area of the rectangle
        """
        return self.__size * self.__size
