#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after : ., ? and :
"""


def text_indentation(text):
    """
prints a text with 2 new lines after specific characters.

Parameters:

    text: the size length of the square

    Returns: text with 2 new lines after specific characters.

    Raises:
    TypeError: text must be a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    specific_char = (".", "?", ":")
    for char in text:
        print(char, end="")
        if char in specific_char:
            print("\n\n")
        continue
