#!/usr/bin/python3
"""Improves BaseGeometry class"""


class BaseGeometry():
    """Raises an exception"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
