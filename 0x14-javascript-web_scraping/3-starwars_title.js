#!/usr/bin/node

const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const EpisodeNum = process.argv[2];

request(API_URL + EpisodeNum, function (_err, _response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});



// This link's endpoint (films/) will get the first dictionary in the API's 'results'
// property's list of dictionaries: 'https://swapi-api.alx-tools.com/api/films/1',
// because 1 was passed to it which is a value we can pass to the cmd line to
// get the dictinary index before extracting a key's(e.g 'title') value from the dict


//  The website to get the API: 'https://swapi-api.alx-tools.com/'
// The code below will give the same output as the one above but we are getting the output
// from the list of dictionaries index number i.e. a key(title) to get the value
// associated with value of the 'title' key of index 0 of the 'results' property.
// While the above implementation adds the ID of each key to the URL(which will be passed
// to the script as argument), and can be used to get any property or key values specified
// in the code:

// const request = require('request')

// const API_URL = 'https://swapi-api.alx-tools.com/api/films/'

// request(API_URL, function (_err, _response, body) {
//     // body = JSON.parse(body);
//     console.log(JSON.parse(body).results[0].title)
// })
