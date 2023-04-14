#!/usr/bin/python3
"""Improves BaseGeometry class"""


class BaseGeometry():
    """Raises an exception and validates integer"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as int and returns exceptions.
        Args:
        name (str): name
        value (int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
