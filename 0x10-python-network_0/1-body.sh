#!/bin/bash
#This script that takes in a URL, sends a GET request to the URL, and displays the body of the response
#If there's a redirect -L tells curl to automatically make subsequent requests to the new location until it reaches the final destination
curl -sL "$1"
