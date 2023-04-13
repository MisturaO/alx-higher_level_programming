#!/usr/bin/python3
"""class named 'MyList' that inherits from 'list'
a subclass of the list class"""


class MyList(list):
    """prints the list, but sorted (ascending sort)"""
    def __init__(self):
        """initializes the class instance"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
