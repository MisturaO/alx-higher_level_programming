#!/usr/bin/python3

if __name__ == "__main__":
    """Executing modules as scripts.Make the file usable
    as a script as well as an importable module.The code 
    that parses the command line only runs if the module 
    is executed as the “main” file
    """
    from add_0 import add

a = 1
b = 2
print("{} + {} = {} ".format(a, b, add(a, b)))
