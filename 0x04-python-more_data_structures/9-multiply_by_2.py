#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    num = 2
    for k, v in list(new_dict.items()):
        new_dict[k] = v * num
    return new_dict
