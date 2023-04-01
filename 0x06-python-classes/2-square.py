#!/usr/bin/python3
"""Square that defines a square by private
instance attribute: size"""


class Square:
    """Validates the size of square"""
    def __init__(self, size=0):
        """Initializes square object.
        
        Args:
            size (int): size of the square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
