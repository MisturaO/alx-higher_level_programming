#!/usr/bin/python3
"""
Displays the value of the 'X-Request-Id' variable found
in the header of the response."""
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    url_req = request.Request(argv[1])
    with request.urlopen(url_req) as response:
        header_values = response.headers
        print(header_values['X-Request-Id'])
