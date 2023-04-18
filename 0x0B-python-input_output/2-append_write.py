#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8):
    Args:
    filename(str):file to write to
    text(str): text to write to file
    Returns: returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
