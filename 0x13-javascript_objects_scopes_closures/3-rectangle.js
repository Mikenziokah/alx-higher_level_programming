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
}
module.exports = Rectangle;
