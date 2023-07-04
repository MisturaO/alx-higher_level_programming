#!/bin/bash
#This script sends a DELETE request to the URL passed as first argument to it and displays the body of the response
curl -sX DELETE "$1"