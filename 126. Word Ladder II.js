/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {string[][]}
 */
var findLadders = function(beginWord, endWord, wordList) {

    var ladders = new Array();
    var map = new Map();
    var distance = new Map();

    wordList.push(beginWord);
    //wordList.push(endWord);

    bfs(map, distance, beginWord, wordList);

    var path = new Array();

    dfs(ladders, path, beginWord, endWord, distance, map);

    return ladders;

    function bfs(map, distance, beginWord, wordList) {
        var q = new Array();
        q.push(beginWord);
        distance.set(beginWord, 0);
        for (var n in wordList) {
            map.set(wordList[n], []);
        }

        while (q.length > 0) {
            var crt = q.shift();
            var nextList = expand(crt, wordList);

            for ( var m in nextList ) {
                map.get(nextList[m]).push(crt);
                if (!distance.has(nextList[m])) {
                    distance.set(nextList[m], distance.get(crt) + 1);
                    q.push(nextList[m]);
                }
            }
        }
    }

    function expand (crt, wordList) {
        var expansion = new Array();

        var letters = 'abcdefghijklmnopqrstuvwxyz';
        for (var i = 0; i < crt.length; i++) {
            for (var j = 0; j < letters.length; j++) {
                if(crt[i] != letters[j]) {
                    var expanded = crt.substring(0, i) + letters[j] + crt.substring(i+1);

                    if (wordList.indexOf(expanded) > -1) {
                        expansion.push(expanded);
                    }
                }
            }
        }
        return expansion;
    }

    function dfs (ladders, path, beginWord, crt, distance, map) {
        path.push(crt);
        if( crt == beginWord ) {
            path.reverse();
            ladders.push(path.slice());
            path.reverse();
        } else {
            var crtList = map.get(crt);
            for (var x in crtList) {
                if (distance.has(crtList[x]) && distance.get(crt) == distance.get(crtList[x]) + 1) {
                    dfs(ladders, path, beginWord, crtList[x], distance, map);
                }
            }
        }
        path.pop();
    }
};