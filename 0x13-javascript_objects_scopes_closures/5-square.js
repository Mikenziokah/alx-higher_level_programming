#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
}
module.exports = Rectangle;
