#!/usr/bin/node
const fs = require('fs');
const argms = process.argv[2];

fs.readFile(argms, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
