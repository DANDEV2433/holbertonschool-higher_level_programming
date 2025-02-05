#!/usr/bin/python3
"""
class VerboseList that inherits from the built-in list class
"""


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with {len[x]} items.")

    def remove(self, item):
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, item):
        super().pop(item)
        print(f"Popped {[item]} from the list.")
