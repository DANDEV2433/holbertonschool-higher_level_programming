#!/usr/bin/python3
"""
import ABC and abstractmethod module abc
"""
from abc import ABC, abstractmethod

"""
Setting up the Abstract Class Animal
"""


class Animal(ABC):
    """
    the Animal class, ensuring it inherits from ABC to mark it as abstract.
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Create a subclass named Dog that inherits from the Animal class.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Create a subclass named Cat that inherits from the Animal class.
    """
    def sound(self):
        return "Meow"
