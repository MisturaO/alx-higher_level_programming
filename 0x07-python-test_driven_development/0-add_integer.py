#!/usr/bin/python3
"""adds 2 integers."""


def add_integer(a, b=98):
    """args are type casted to int or float.
    Raises:
            TypeError(If either are non int or non float)

    Returns:
            the addition of a and b
    """
    if((not isinstance(a, float) and not isinstance(a, int))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
