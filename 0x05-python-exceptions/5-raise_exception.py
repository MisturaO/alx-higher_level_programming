#!/usr/bin/python3

def raise_exception():
    """raises a type exception."""
    try:
        raise TypeError
    except TypeError:
        raise
