#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples."""
    new_tuple = ()
    new_1 = tuple_a + (0, 0)
    new_2 = tuple_b + (0, 0)
    new_tuple = new_1[0] + new_2[0], new_1[1] + new_2[1]
    return(new_tuple)
