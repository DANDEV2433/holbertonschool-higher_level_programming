#!/usr/bin/python3
"""
Module JSON, Write a function that writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a function that writes an Object to a text file
    """
    with open(filename, "w", encoding="utf_8") as file:
        json.dump(my_obj, file)
