#!/usr/bin/python3
"""Defines the Base class"""
import json


class Base:
    """The Base class

    This class is the “base” of all other classes in this project

    Private class attribute:
        __nb_objects (int):Number of Bases class instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base
        Args:
            id (int): The identity of the Base instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list of dictionaries.
        Otherwise,return the '[]'"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_list = json.dumps(list_dictionaries)
            return json_list

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs"""
        list_i = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for i in list_objs:
                    list_i.append(i.to_dictionary())
            f.write(cls.to_json_string(list_i))

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string representation and returns it as python data
        (This returns the deserialization of a JSON string).
        Args:
           json_string(str): json_string is a string representing
           a list of dictionaries"""
        if json_string:
            return json.loads(json_string)
        else:
            return []
