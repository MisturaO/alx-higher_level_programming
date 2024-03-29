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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the rectangle's 'x' coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get the rectangle's 'y' coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle"""
        rect_area = self.__width * self.__height
        return rect_area

    def display(self):
        """prints in stdout the Rectangle instance with the character '#'"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
        """Tried other implementations nested loop and list comprehension:
        Nested Loop:
        for _ in range(self.y):
            print()
        for _ in range(self.height):
           for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
               print("#", end="")
            print()
        List comprehension:
        [print() for _ in range(self.y)]
        [print(" " * self.x + "#" * self.width) for _ in range(self.height)]
        """
    def __str__(self):
        """
        Overriding the __str__ method so that it returns a readable output:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height))

    def update(self, *args, **kwargs):
        """
        Assigns a “no-keyword argument(*args)” and a
        “keyword argument(*kwargs)”to each class attribute:
        NOTE: Argument order is super important.**kwargs must
        be skipped if *args exists and is not empty.
        Args:
            *args(int): assigns args to attributes
            *kwargs(int): assigns args to attrs if len is not empty
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """Creates and returns the dictionary representation
        of Rectangle class(i.e. converts attributes of Rectangle
        class into dictionary representation)"""
        return({"id": self.id, "width": self.width, "height": self.height,
               "x": self.x, "y": self.y})
