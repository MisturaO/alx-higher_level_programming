#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """Returns True if obj is directly or indirectly an
    instance of a_class and False otherwise"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
