#!/usr/bin/python3
"""
Module JSON that returns an object (Python data structure)
"""
import json


def from_json_string(my_str):
    """
    Write a function that returns an object (Python data structure)
    represented by a JSON string:
    """
    json_string = json.loads(my_str)
    return (json_string)
