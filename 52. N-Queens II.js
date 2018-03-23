/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    var result = [];

    dfs(n, result, []);

    return result.length;
};

var dfs = function (n, result, tmp) {
    if (tmp.length == n) {
        result.push(tmp.slice());
        return
    }

    for (var i = 0; i < n; i++) {
        if (isValid(tmp, i)) {
            tmp.push(i);
            dfs(n, result, tmp);
            tmp.pop();
        }
    }
};

var isValid = function (tmp, i) {
    var n = tmp.length;
    for (var j = 0; j < n; j++) {
        if (tmp[j] == i) {
            return false;
        }
        if (tmp[j] + j == i + n) {
            return false;
        }
        if (tmp[j] - j == i - n) {
            return false;
        }
    }
    return true;
};