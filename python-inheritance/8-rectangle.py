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
