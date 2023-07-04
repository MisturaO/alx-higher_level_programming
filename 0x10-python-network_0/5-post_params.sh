#!/bin/b
#Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the responses
curl -sX POST -H "Content_Lenght: 35" -H "Content_Type: mime-type" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
