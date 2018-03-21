/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {

    var result = [];
    if ( digits == null || digits.length == 0 ) {
        return result;
    }

    var map = new Map();
    map.set(0, []);
    map.set(1, []);
    map.set(2, ['a','b','c']);
    map.set(3, ['d','e','f']);
    map.set(4, ['g','h','i']);
    map.set(5, ['j','k','l']);
    map.set(6, ['m','n','o']);
    map.set(7, ['p','q','r','s']);
    map.set(8, ['t','u','v']);
    map.set(9, ['w','x','y','z']);

    dfs(digits, map, result, "");

    return result;
};

var dfs = function (digits, map, result, str) {
    if (str.length == digits.length) {
        result.push(str.toString());
        return;
    }

    var n = str.length;
    var number = parseInt(digits[n]);
    var arr = map.get(number);

    for (var d of arr) {
        str += d;
        dfs(digits, map, result, str);
        str = str.slice(0, str.length-1);
    }
};