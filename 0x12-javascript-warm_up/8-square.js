#!/usr/bin/node
//  prints a square

const squareSize = parseInt(process.argv[2]);
let char = '';
if (!squareSize) {
  console.log('Missing size');
}

for (let i = 0; i < squareSize; i++) {
  char += 'X';
}

for (let i = 0; i < squareSize; i++) {
  console.log(char);
}
