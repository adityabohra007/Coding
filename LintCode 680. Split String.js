/**
 * Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.
 * @param s
 * @returns {Array}
 *
 * Examples:
 * Given the string "123"
   return [["1","2","3"],["12","3"],["1","23"]]
 */
const splitString = function (s) {
    var result = [];
    if (s == null) {
        return result;
    } else if (s.length == 0) {
        result.push([]);
        return result;
    }

    dfs(s, result, 0, []);

    return result;
};

const dfs = function (s, result, index, tmp) {
    if (index == s.length) {
        result.push(tmp.slice());
        return;
    }

    for (var i=index; i < index+2 && i < s.length; i++) {
        var subString = s.substring(index, i+1);
        tmp.push(subString);
        dfs(s, result, i+1, tmp);
        tmp.pop();
    }
};