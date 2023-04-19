#!/usr/bin/python3
"""A 'Class Student' that retrieves the dictionary representation
of its instance"""


class Student:
    """Defines a student attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        Arg:
            attr (dict): If attrs is a list of strings, only attribute names
            contained in this list must be retrieved.Otherwise, all
            attributes must be retrieved
        """
        dict_rep = self.__dict__.copy()
        if type(attrs) is list:
            for value in attrs:
                if type(value) is not str:
                    return dict_rep
            dict_list = {}

            for val in range(len(attrs)):
                for dict_s in dict_rep:
                    if attrs[val] == dict_s:
                        dict_list[dict_s] = dict_rep[dict_s]
            return dict_list
        return dict_rep
