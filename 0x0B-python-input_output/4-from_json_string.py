#!/usr/bin/python3
"""a function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Function that returns a python object from a json string.
    Args:
        my_str (str): Takes json string.
    """
    python_object = json.loads(my_str)
    return python_object
