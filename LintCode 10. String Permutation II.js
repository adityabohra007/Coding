/**
 * @param str: A string
 * @return: all permutations
 */
const stringPermutation2 = function (str) {

    var result = [];
    if (str == null || str.length == 0) {
        return [""];
    }

    var strArr = [];
    var used = [];
    for (var i = 0; i < str.length; i++) {
        strArr.push(str[i]);
        used.push(false);
    }

    strArr.sort();

    dfs(strArr, result, "", used);

    return result;
};

const dfs = function (strArr, result, tmp, used) {
    if (tmp.length == strArr.length) {
        result.push(tmp.toString());
        return;
    }

    for (var j = 0; j < strArr.length; j++) {
        if (used[j] || (j != 0 && strArr[j] == strArr[j-1] && !used[j - 1])) {
            continue;
        }
        tmp += strArr[j];
        used[j] = true;
        dfs(strArr, result, tmp, used);
        tmp = tmp.slice(0, tmp.length-1);
        used[j] = false;
    }
};
