#!/usr/bin/node
//  prints the addition of 2 integers of the first and second cmd line args
const i = parseInt(process.argv[2]);
const x = parseInt(process.argv[3]);

function add(a, b) {
  result = a + b;
  return result;
}
console.log(add(i, x));
