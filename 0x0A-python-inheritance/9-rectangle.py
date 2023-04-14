#!/usr/bin/python3
"""Rectangle class inherits from BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle validated by BaseGeometry integer_validator method"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Parent class area() method implementation"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Returns a string of the division of width and height"""
        return ("[{}] {}/{}".format(type(self).__name__, self.__width, self.__height))
