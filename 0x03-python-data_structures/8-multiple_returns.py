#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character."""
    if sentence == " ":
        sentence[0] = None
    else:
        return (len(sentence), sentence[0])
