#!/usr/bin/python3
"""
class CountedIterator
"""


class CountedIterator:
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.count = len(iterator)
        self.current = 0

    def get_count(self):
        return self.current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            self.current += 1
            return next(self.iterator)
        else:
            raise StopIteration
