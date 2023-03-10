def islower(c):
    letter = ord(c)
    if letter in range(97, 123):
	    return True
    elif letter in (65, 92):
        return False
