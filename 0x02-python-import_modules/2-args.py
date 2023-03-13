#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    """prints the number of and the list of its arguments"""

    lenght = len(argv) - 1

    if lenght == 0:
        print("{} arguments.".format(lenght))
    elif lenght == 1:
        print("{} argument:".format(lenght))
    else:
        print("{} arguments.".format(lenght))
    for num in range(lenght):
        print("{}: {}".format(num + 1, argv[num + 1]))
