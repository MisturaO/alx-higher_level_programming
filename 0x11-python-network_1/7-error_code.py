#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response:
If the HTTP status code is greater than or equalto 400,
print: Error code: followed by the value of the HTTP status code
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print("{}".format(response.text))
