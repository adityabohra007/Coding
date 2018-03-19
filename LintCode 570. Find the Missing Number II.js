/**
 * Giving a string with number from 1-n in random order, but miss 1 number.Find that number.
 * Example
   Given n = 20, str = 19201234567891011121314151618
   return 17
 */
const findMissing2 = function (n, str) {
    if (str == null || str.length == 0) {
        return null;
    }

    var result = [];
    dfs(str, 0, result, [], n);

    var ret = result[0];
    ret.sort(function (a, b) {
        return a - b;
    });

    if ( ret[0] != 1 ) {
        return 1;
    } else {
        for ( var j=1; j<ret.length; j++ ) {
            if (ret[j] - ret[j-1] > 1) {
                return ret[j]-1;
            }
        }
    }
};

const dfs = function (str, index, result, tmp, n) {
    if (tmp.length > n-1) {
        return;
    }
    if (index == str.length) {
        result.push(tmp.slice());
        return;
    }

    for (var i = index; i < index+2 && i < str.length; i++) {
        var subString = str.substring(index, i+1);
        var value = parseInt(subString);
        if ( value > 0 && value <= n && tmp.indexOf(value) < 0 ) {
            tmp.push(value);
            dfs(str, i+1, result, tmp, n);
            tmp.pop();
        }
    }
};