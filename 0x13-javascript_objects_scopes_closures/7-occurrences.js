#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let allOccurences = 0;
  let x = 0;
  for (x; x < list.length; x++) {
    if (searchElement === list[x]) {
      allOccurences++;
    }
  }
  return allOccurences;
};
