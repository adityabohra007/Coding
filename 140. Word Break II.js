/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 */
var wordBreak = function(s, wordDict) {
    var result = [];
    if (s == null || s.lenght == 0) {
        return result;
    }

    dfs(s, wordDict, result, "", 0);

    return result;
};

var dfs = function(s, wordDict, result, item, start) {
    if (start >= s.length) {
        result.push(item);
        return;
    }

    var str = "";
    for (var i = start; i < s.length; i++) {
        str = s.substring(start, i+1);
        if (wordDict.indexOf(str) >= 0) {
            var newItem = "";
            if (item.length > 0) {
                newItem = item+" "+str;
            } else {
                newItem = str;
            }
            dfs(s, wordDict, result, newItem, i+1);
        }
    }
};