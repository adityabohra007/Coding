/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {

    if ( s == null || s.length == 0 ) {
        return true
    }

    s = s.toLowerCase();

    var start = 0;
    var last = s.length - 1;

    while ( start <= last ) {
        while ( start < s.length && !isValid(s[start]) ) {
            start++;
        }
        if ( start == s.length ) {
            return true;
        }
        while ( last >= 0 && !isValid(s[last]) ) {
            last--;
        }
        if ( s[start] != s[last] ) {
            return false;
        } else {
            start++;
            last--;
        }
    }
    return true;
};

var isValid = function (char) {
    var code = char.charCodeAt(0);
    if ( (code >= 97 && code <= 122) || (code >= 65 && code <= 90) || (code >= 48 && code <= 57) ) {
        return true;
    } else {
        return false;
    }
};