/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength_1 = function(beginWord, endWord, wordList) {
    if ( wordList == null || wordList.length == 0 ) {
        return 0;
    }

    if ( beginWord == endWord ) {
        return 1;
    }

    var queue = [];
    var tmp = [];

    queue.push( beginWord );
    tmp.push(beginWord);

    var length = 1;
    while ( queue.length > 0 ) {
        length++;
        var size = queue.length;
        for ( var k = 0; k < size; k++ ) {
            var word = queue.shift();
            var nextWords = getNextWords(word, wordList);
            if (nextWords.length > 0) {
                for (var i = 0; i < nextWords.length; i++) {
                    if (nextWords[i] == endWord) {
                        return length;
                    }

                    if (tmp.indexOf(nextWords[i]) > -1) {
                        continue;
                    }

                    queue.push(nextWords[i]);
                    tmp.push(nextWords[i]);
                }
            }
        }
    }
    return 0;

    function getNextWords( word, wordList )
    {
        var nextWords = [];
        for ( var i = 0; i < 26; i++ ) {
            for ( var j = 0; j < word.length; j++ ) {
                var char = String.fromCharCode( 'a'.charCodeAt(0) + i );
                if ( char == word.charAt(j) ) {
                    continue;
                }
                var nextWord = replace( word, j, char );
                if ( wordList.indexOf( nextWord ) > -1 ) {
                    nextWords.push( nextWord );
                }
            }
        }

        return nextWords;
    }

    function replace ( word, pos, char )
    {
        var wordTmp = word.split('');
        wordTmp[pos] = char;
        wordTmp = wordTmp.join('');
        return wordTmp;
    }
};

// BFS 解法
var ladderLength_2 = function(beginWord, endWord, wordList) {
    var visited = new Set();
    var queue = [];
    var level = 1;
    var letters = 'abcdefghijklmnopqrstuvwxyz';
    queue.push(beginWord);
    visited.add(beginWord);

    while(queue.length > 0) {

        var len = queue.length;

        for(var i = 0; i < len; i++) {
            var word = queue.shift();

            for(var j = 0; j < word.length; j++) {
                for(var k = 0; k < letters.length; k++) {
                    var newWord = word.substring(0, j) + letters[k] + word.substring(j + 1);

                    if(wordList.indexOf(newWord) < 0) {
                        continue;
                    }

                    if(newWord === endWord) {
                        return level + 1;
                    }
                    if(wordList.indexOf(newWord) > -1 && !visited.has(newWord)) {
                        queue.push(newWord);
                        visited.add(newWord);
                    }
                }
            }
        }
        level++;
    }

    return 0;
};