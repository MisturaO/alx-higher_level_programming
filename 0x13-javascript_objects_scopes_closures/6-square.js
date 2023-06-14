#!/usr/bin/node
//  Square class that inherits from 5-square.js
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let char = '';
      for (let i = 0; i < this.height; i++) {
        char += c;
      }
      console.log(char);
    }
  }
}

module.exports = Square;
