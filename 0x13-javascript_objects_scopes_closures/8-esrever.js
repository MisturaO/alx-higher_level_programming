#!/usr/bin/node
//  Returns the reversed version of a list

exports.esrever = function (list) {
  let listLen = list.length - 1;
  let i = 0;
  for (i; listLen > i; i++) {
    const temp = list[listLen];
    list[listLen] = list[i];
    list[i] = temp;
    listLen--;
  }
  return list;
};
