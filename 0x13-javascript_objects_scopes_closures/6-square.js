#!/usr/bin/node
const Square = require('./6-square');

class Square extends Square {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.side; i++) {
      let row = '';
      for (let j = 0; j < this.side; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
