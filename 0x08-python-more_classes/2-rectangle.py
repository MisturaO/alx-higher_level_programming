#!/usr/bin/python3
"""An class Rectangle that defines a rectangle"""


class Rectangle():
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        self.a = self.height * self.width
        return self.a

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            self.perim = 0
        else:
            self.perim = (self.height * 2) + (self.width * 2)
        return self.perim
