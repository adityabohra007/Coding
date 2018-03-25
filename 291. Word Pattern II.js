/**
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPatternMatch = function(pattern, str) {
    var map = new Map();
    var set = new Set();

    return match(pattern, str, map, set);
};

var match = function(pattern, str, map, set) {
    if (pattern.length == 0) {
        return str.length == 0;
    }

    var c = pattern[0];
    if (map.has(c)) {
        if (!str.startsWith(map.get(c))) {
            return false;
        }

        return match(pattern.substring(1), str.substring(map.get(c).length), map, set);
    }

    for (var i = 0; i < str.length; i++) {
        var word = str.substring(0, i+1);
        if (set.has(word)) {
            continue;
        }
        map.set(c, word);
        set.add(word);
        if (match(pattern.substring(1), str.substring(i+1), map, set)) {
            return true;
        }
        set.delete(word);
        map.delete(c);
    }
    return false;
};