#!/usr/bin/python3
"""
basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON file
and deserialize the JSON file to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf_8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
