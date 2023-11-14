#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;
    for (x; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rec = this.width;
    this.width = this.height;
    this.height = rec;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
