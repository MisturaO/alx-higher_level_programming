#!/usr/bin/node
//  converts a number from base 10 to another base passed as argument

exports.converter = function (base) {
    function num (i) {
        return i.toString(base);
    }
    return num;
}
