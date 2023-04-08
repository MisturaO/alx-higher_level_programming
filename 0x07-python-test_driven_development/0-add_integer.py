#!/usr/bin/python3
"""adds 2 integers."""


def add_integer(a, b=98):
    """args are type casted to int or float.
    Raises:
            TypeError(If either are non int or non float)

    Returns:
            the addition of a and b
    """
    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
