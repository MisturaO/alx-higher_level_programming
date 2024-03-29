#!/usr/bin/node
//  Create an instance method called print() that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let char = '';
      for (let j = 0; j < this.width; j++) {
        char += 'X';
      }
      console.log(char);
    }
  }
}

module.exports = Rectangle;
