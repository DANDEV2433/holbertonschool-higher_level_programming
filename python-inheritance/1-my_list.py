#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted
        """
        print(sorted(self))
