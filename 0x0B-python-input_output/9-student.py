#!/usr/bin/python3
"""A 'Class Student' that retrieves the dictionary representation
of its instance"""


class Student:
    """Defines a student attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__