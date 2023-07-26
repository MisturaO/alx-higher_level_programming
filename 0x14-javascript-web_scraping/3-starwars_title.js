#!/usr/bin/node

const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const EpisodeNum = process.argv[2];

request(API_URL + EpisodeNum, function (_err, _response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
