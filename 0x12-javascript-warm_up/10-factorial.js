#!/usr/bin/node

function factorial (i) {
  if (i === 0 || !Number(i)) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
