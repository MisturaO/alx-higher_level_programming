#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list."""
    if idx < 0:
        return my_list
    elif my_list[idx] > len(my_list):
        return my_list
    else:
        del my_list[idx]
    return my_list
