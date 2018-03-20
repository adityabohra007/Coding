/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    var result = [];
    var l = 0;
    var r = 0;

    for (var i = 0; i < s.length; i++) {
        if (s[i] == '(') {
            l++;
        }
        if (s[i] == ')') {
            if (l > 0) {
                l--;
            } else {
                r++;
            }
        }
    }

    dfs(s, result, l, r, 0);

    return result;
};

var dfs = function (s, result, l, r, index) {
    if ( l == 0 && r == 0 ) {
        if ( isValid(s) ) {
            result.push(s);
        }
        return;
    }

    for (var i=index; i<s.length; i++) {
        if (i != index && s[i] == s[i-1]) {
            continue;
        }

        if (s[i] == '(') {
            var subString = s.substring(0, i) + s.substring(i+1);
            if (l > 0) {
                dfs(subString, result, l-1, r, i);
            }
        }

        if (s[i] == ')'){
            var subString = s.substring(0, i) + s.substring(i+1);
            console.log(subString);
            if (r > 0) {
                dfs(subString, result, l, r-1, i);
            }
        }
    }
};

var isValid = function (s) {
    var count = 0;
    for (var j=0; j<s.length; j++) {
        if (s[j] == '(') {
            count++;
        }
        if (s[j] == ')') {
            count--;
            if (count < 0) {
                return false;
            }
        }
    }

    return count == 0;
};