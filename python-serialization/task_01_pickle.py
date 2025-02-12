#!/usr/bin/python3
"""
Learn how to serialize and deserialize custom Python objects
using the pickle module
"""
import json
import pickle


class CustomObject():
    def __init__(self, name, age, is_student):
        self.name = name  # string
        self.age = age  # integer
        self. is_student = is_student  # boolean

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"is_student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open('filename', 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open('filename', 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
