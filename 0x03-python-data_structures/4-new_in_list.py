#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in a list without modifying the original list"""
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
