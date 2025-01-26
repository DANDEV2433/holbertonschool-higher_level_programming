#!/usr/bin/python3
"""
Module that prints first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """
print first name and last name with fonction say_my_name

Parameters:

    first_name: character string containing first_name
    last_name: character string containing last_name

    Returns:
    the first_name and the last_name

    Raises:
    TypeError: first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str) or first_name.isdigit():
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
