#!/usr/bin/python3
"""Lookup function to get the list of available
class attributes and methods"""


def lookup(obj):
    """returns the list of available attributes
    and methods of an object"""
    return(dir(obj))
