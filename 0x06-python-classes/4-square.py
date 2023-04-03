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
        self.size = size

    @property
    def size(self):
        """Gets and sets the value of the square.
        This access and updates private attribute __size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Gets current square area.
        Returns:
            returns the current square area
        """
        return self.__size * self.__size
