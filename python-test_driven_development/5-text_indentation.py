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
    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in specific_char:
            print("\n\n", end="")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1  # Incrémenter seulement si ce n'est pas un caractère spécifique
