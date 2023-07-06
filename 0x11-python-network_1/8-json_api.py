#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv

if __name__ == "__main__":
    letter = ''
    if len(argv) > 1:
        letter = argv[1]
    data = {'q': letter}
    
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        content = response.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get('id'), content.get('name')))
            
    except ValueError:
        print("Not a valid JSON")
