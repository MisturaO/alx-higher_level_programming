#!/usr/bin/node
// computes and prints a factorial

const arg = Number(process.argv[2]);

function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  }
  if (a < 0) {
    return (-1);
  }
  return (a * factorial(a - 1));
}
console.log(factorial(arg));
