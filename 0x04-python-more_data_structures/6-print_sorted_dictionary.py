#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
