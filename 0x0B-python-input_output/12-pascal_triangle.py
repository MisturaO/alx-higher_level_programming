#!/usr/bin/python3
"""
A function def pascal_triangle(n): that returns a
list of lists of integers representing the Pascal’s
triangle of n
"""


def pascal_triangle(n):
    res = []
    if n <= 0:
        return res
    for a in range(n):
        row = []
        column = 1
        for b in range(a+1):
            row.append(column)
            column = column * (a - b) // (b + 1)
        res.append(row)
    return res
