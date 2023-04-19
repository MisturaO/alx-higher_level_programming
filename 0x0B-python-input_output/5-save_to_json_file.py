#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using json
    representation
    Args:
        my_object (string): Takes python objects
        filename(string): json file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
