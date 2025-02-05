#!/usr/bin/python3
"""
import ABC and abstractmethod module abc
import module math for mathematical functions
"""
from abc import ABC, abstractmethod
import math

"""
Setting up the Abstract Class Shape
"""


class Shape(ABC):
    """
    the Shape class, ensuring it inherits from ABC to mark it as abstract.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    concrete class Circle inheriting from Shape
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    concrete class Rectangle inheriting from Shape
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(Shape):
    print("area: {}".format(Shape.area()))
    print("perimeter: {}".format(Shape.perimeter()))
