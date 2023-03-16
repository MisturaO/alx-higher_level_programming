#!/usr/bin/python3

def max_integer(my_list=[]):
    """finds the biggest integer of a list."""
    max_1 = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for i in range(1, len(my_list)):
            if my_list[i] > max_1:
                max_1 = my_list[i]
        return max_1
