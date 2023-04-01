#!/usr/bin/python3

"""Square that defines a square by private
instance attribute: size"""


class Square:
    """Validates the size of square"""
    def __init__(self, size=0):
        """Initializes square object.
        Args:
            size (int): size of the square object.
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Gets current square area.
        Returns:
            returns the current square area
        """
        self.__size = self.__size * self.__size
        return self.__size
