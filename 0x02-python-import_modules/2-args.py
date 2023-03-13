#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of it    s arguments"""
    import sys

    lenght = len(sys.argv) - 1
    if lenght == 0:
        print("{} arguments.".format(lenght))
    elif lenght == 1:
        print("{} argument:".format(lenght))
    else:
        print("{} arguments.".format(lenght))
    for num in range(lenght):
        print("{}: {}".format(num + 1, sys.argv[num + 1]))
