/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {

    var result = 0;
    if ( s == null || s.length == 0 ) {
        return result;
    }

    var map = new Map();
    var n = s.length;
    for ( var i = 0; i < n; i++ ) {
        if ( map.get(s[i]) ) {
            var value = map.get(s[i]) + 1;
            map.set(s[i], value);
        } else {
            map.set(s[i], 1);
        }
    }

    var haveOne = false;
    for ( var v of map.values() ) {
        if ( v == 1 ) {
            if ( !haveOne ) {
                result++;
                haveOne = true;
            }
        } else if ( v%2 ) {
            if ( !haveOne ) {
                result = result + v;
                haveOne = true;
            } else {
                result = result + v - 1;
            }
        } else {
            result = result + v;
        }
    }

    return result;
};