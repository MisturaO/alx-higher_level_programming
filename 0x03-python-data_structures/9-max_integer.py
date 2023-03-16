#!/usr/bin/python3

def max_integer(my_list=[]):
    """finds the biggest integer of a list."""
    large_num = my_list[0]
    if len(my_list) == 0:
        return "None"
    else:
        for num in my_list:
            if num > large_num:
                large_num = num
        return large_num
