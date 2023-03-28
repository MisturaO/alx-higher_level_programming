#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list. """
    sum_all = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            sum_all += 1
        except IndexError:
            break
    print("")
    return sum_all
