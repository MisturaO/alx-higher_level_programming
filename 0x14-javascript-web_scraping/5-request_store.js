#!/usr/bin/node
const fs = require('fs');

const request = require('request');

// This script gets the contents of a webpage and stores it in a file.
const UrlReq = process.argv[2];
const FilePath = process.argv[3];

request(UrlReq, function (_error, _response, body) {
//   body = JSON.parse(body);
  // console.log(body);
    fs.writeFileSync(FilePath, body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
});