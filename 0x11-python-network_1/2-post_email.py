#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import urllib.request as request
from sys import argv
import urllib.parse as parse

if __name__ == "__main__":
    url_req = request.Request(argv[1])
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode()
    with request.urlopen(url_req, data) as response:
        print("{}".format(response.read().decode()))
