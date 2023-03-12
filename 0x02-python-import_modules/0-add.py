#!/usr/bin/python3

if __name__ == "__main__":
    """The code that parses the command line only runs if the module 
    is executed as the “main” file"""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {} ".format(a, b, add(a, b)))
