#!/usr/bin/python3
"""
module write function that appends a string at the end
"""


def append_write(filename="", text=""):
    """
    Write a function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added:
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
