#!/usr/bin/python3

def safe_print_integer(value):
    """function that prints an integer with "{:d}".format()"""
    try:
        print("{:d}".format(value))
    except ValueError:
        pass
    if isinstance(value, int):
        return True
    else:
        return False
