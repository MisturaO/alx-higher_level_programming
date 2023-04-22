#!/usr/bin/python3
"""Class "Rectangle" inherits fron "Base" class.
With private instance attributes, each with its
own public getter and setter"""
from models.base import Base


class Rectangle(Base):
    """Inherited class 'Rectangle' """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle instances
        Args:
            id(int):The Rectangle's identity
            width(int): Rectangle's width
            height(int): Rectangle's height
            x(int): The x coordinate of the rectangle
            y(int): The y coordinate of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(self.__width))
        if value <= 0:
            raise ValueError("{} must be > 0".format(self.__width))
        self.__width = value

    @property
    def height(self):
        """set/get the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(self.__height))
        if value <= 0:
            raise ValueError("{} must be > 0".format(self.__height))
        self.__height = value

    @property
    def x(self):
        """set/get the rectangle's 'x' coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(self.__x))
        if value < 0:
            raise ValueError("{} must be >= 0".format(self.__x))
        self.__x = value

    @property
    def y(self):
        """set/get the rectangle's 'y' coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(self.__y))
        if value < 0:
            raise ValueError("{} must be >= 0".format(self.__y))
        self.__y = value
