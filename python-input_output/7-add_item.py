#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list,
and then save them to a file
"""
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"


def add_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file)
