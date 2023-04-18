#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of python  object
    Args:
    my_obj (str): Takes python string
    """
    json_rep_object = json.dumps(my_obj)
    return json_rep_object
