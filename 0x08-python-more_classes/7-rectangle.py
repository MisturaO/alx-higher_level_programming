#!/usr/bin/python3
"""A Rectangle class that defines a rectangle"""


class Rectangle():
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get and set the width of the rectangle"""
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
        """Get and set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        self.a = self.height * self.width
        return self.a

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            self.perim = 0
        else:
            self.perim = (self.height * 2) + (self.width * 2)
        return self.perim

    def __str__(self):
        """prints string representation of the rectangle"""
        rec_string = ""
        if self.width == 0 or self.height == 0:
            return("")
        rec_string += "\n".join(str(self.print_symbol) * self.__width
                                for i in range(self.__height))
        return rec_string

    def __repr__(self):
        """Returns a string representation of the rectangle
        so as to recreate a new instance by using evalwhen 
        creating instances:
        Rectangle(arg1, arg2)"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """deletes an instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
