#!/usr/bin/python3
"""
Making a GET request with the 'requests' module:
This module has methods for GET, POST, DELETE etc and doesn't
requires some extra step we use in the 'urllib.request' module.

This Python script fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    """
    Makes a request with 'get()' and authomatically gets the body
    response from the server, which is stored in the 'response' var.
    'requests' will authomatically decode the body's content.
    """
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")

    """Prints the data type of the body"""
    print("\t- type: {}".format(type(response.text)))
    """prints the content of the body"""
    print("\t- content: {}".format(response.text))
