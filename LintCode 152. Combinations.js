/**
 * @param n: Given the range of numbers
 * @param k: Given the numbers of combinations
 * @return: All the combinations of k numbers out of 1..n
 */
const combine = function (n, k) {
    var result = [];

    dfs (n, k, result, [], 1);

    return result;
};

const dfs = function(n, k, result, tmp, index) {
    if (tmp.length == k) {
        result.push(tmp.slice());
        return;
    }

    for (var i=index; i <= n; i++ ) {
        tmp.push(i);
        dfs(n, k, result, tmp, i+1);
        tmp.pop();
    }
};

