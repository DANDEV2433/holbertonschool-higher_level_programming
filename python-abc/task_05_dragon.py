#!/usr/bin/python3
"""
class named Dragon that inherits from both SwimMixin and FlyMixin.
"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def __init__(self):
        self.Draco = 'Draco'

    def roar(self):
        print(f"the dragon {self.Draco} roars!")

    def fire(self):
        print(f"the dragon {self.Draco} spits fire")
