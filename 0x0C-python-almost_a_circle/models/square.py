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
        return("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        Assigns args to class attrs through *args and *kwargs.
        **kwargs must be skipped if *args exists and is not empty:
            Args:
                *args is the list of arguments - no-keyworded arguments:
                    1st argument should be the id attribute
                    2nd argument should be the size attribute.
                    3rd argument should be the x attribute.
                    4th argument should be the y attribute
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Creates and returns the dictionary representation
         of Square class/instance attributes"""
        return({"id": self.id, "size": self.size, "x": self.x, "y": self.y})
