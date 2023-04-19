#!/usr/bin/python3
"""A function that returns the dictionary description of a class"""


def class_to_json(obj):
    """obj is a class instance"""
    return obj.__dict__
