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

    @classmethod
    def create(cls, **dictionary):
        """Returns instance of the child class with all
        attributes already set:
            Rectangle: takes "width and height" values.
            Square: takes"size" which has the values of
            both"width and height" stored in attribute size"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy_instance = cls(1)
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances:
            If the file doesn’t exist, return an empty list
            Otherwise, return a list of instances -
            the type of these instances depends on cls (current
            class using this method)"""
        instance_list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                instances = cls.from_json_string(f.read())
        except:
            []
        for instance in instances:
            var = cls.create(**instance)
            instance_list.append(var)
        return instance_list
