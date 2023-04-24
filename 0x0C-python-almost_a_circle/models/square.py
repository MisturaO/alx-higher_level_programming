#!/usr/bin/python3
"""
Square is a special Rectangle, so it makes sense this
class Square inherits from Rectangle. Now you have a
Square class who has the same attributes and same methods.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """calls the Rectangle class attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The value of size is assigned to width and height
        and either of them is returned. in this case 'height'
        is returned"""
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return("[{}] {} {}/{} - {}".format(type(self).__name__, self.id,
                                           self.x, self.y, self.size))
