#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request as request
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    url_req = request.Request(argv[1])

    try:
        with request.urlopen(url_req) as response:
            print("{}".format(response.read().decode('utf-8')))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
