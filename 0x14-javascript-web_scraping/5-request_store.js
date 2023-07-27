#!/usr/bin/node
const fs = require('fs');

const request = require('request');

// This script gets the contents of a webpage and stores it in a file:
//   first arg: URL to request
//  second arg: the file path to store the body response
//  The file is UTF-8 encoded

const UrlReq = process.argv[2];
const FilePath = process.argv[3];

request(UrlReq, function (_error, _response, body) {
// if the link passed to the script is not in JSON (e.g HTML) format and you try to deserialize,it will return error
//   body = JSON.parse(body);
  // console.log(body);
  fs.writeFile(FilePath, body, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
