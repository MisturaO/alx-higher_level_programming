#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a
POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.

Posts an email to the server and prints out the server response body
"""
import requests
from sys import argv

if __name__ == "__main__":
    """Content to send to the server"""
    email = {'email': argv[2]}

    """Post the content to the server via the URL in argv[1]
    and gets server's reponse"""
    response = requests.post(argv[1], email)
    """Print out the body of the server's reponse"""
    print("{}".format(response.text))
