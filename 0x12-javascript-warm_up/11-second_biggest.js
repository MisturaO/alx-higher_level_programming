#!/usr/bin/node
//  searches the second biggest integer in the list of arguments.


if (process.argv.length === 2) {
    console.log(0);
}else if (process.argv.length === 3) {
    console.log(0);
} else {
    const args = process.argv.length;
    const nums = [];
    for (let i = 2; i < args; i++) {
        nums[i - 2] = parseInt(process.argv[i]);
    }
    nums.sort((a, b) => {return b - a;});
    console.log(nums[1]);
}
