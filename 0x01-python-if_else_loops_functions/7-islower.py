#!/usr/bin/python3
def islower(c):
    letter = ord(c)
    if letter in range(97, 123):
        return True
    else:
        return False
