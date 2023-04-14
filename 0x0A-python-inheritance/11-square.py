#!/usr/bin/python3
"""Square class that inherits from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of square"""
        area = self.__size ** 2
        return area

    def __str__(self):
        """str() returns the square description"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__size, self.__size)
