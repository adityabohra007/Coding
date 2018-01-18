/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    var result = [];
    if ( s == null || s.length == 0 ) {
        return result;
    }

    dfs(s, 0, result, []);

    return result;

    function dfs( str, startIndex, result, tmp ){
        if ( startIndex == str.length ) {
            result.push(tmp.slice());
        }

        for ( var i = startIndex; i < str.length; i++ ) {
            var subString = str.slice(startIndex, i + 1);
            if ( !isPalindrome(subString) ) {
                continue;
            }
            tmp.push(subString);
            dfs(str, i + 1, result, tmp);
            tmp.pop();

        }
    }

    function isPalindrome ( str ) {
        if ( str == null || str.length == 0 ) {
            return false;
        }

        for ( var i = 0; i < str.length; i++ ) {
            if ( str[i] != str[str.length - 1 - i] ) {
                return false;
            }

            if ( i == str.length - i ) {
                break;
            }
        }

        return true;
    }
};