#!/usr/bin/python3
"""
Learn how to serialize and deserialize custom Python objects
using the pickle module
"""
import pickle


class CustomObject():
    """
    custom Python class named CustomObject
    """
    def __init__(self, name, age, is_student):
        self.name = name  # string
        self.age = age  # integer
        self. is_student = is_student  # boolean

    def display(self):
        """
        method display method to print out the object’s attributes
        with the following format:
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"is_student: {self.is_student}")

    def serialize(self, filename):
        """
        This method will take a filename as its parameter.
        Using the pickle module, it will serialize the current instance
        of the object and save it to the provided filename.
        """
        try:
            with open('filename', 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        This class method will take a filename as its parameter.
        Using the pickle module, it will load and return
        an instance of the CustomObject from the provided filename.
        """
        try:
            with open('filename', 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
