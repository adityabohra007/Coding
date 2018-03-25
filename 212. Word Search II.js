/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    var tire = new Trie();
    for (var word of words) {
        tire.insert(word);
    }

    var m = board.length;
    var n = board[0].length;
    var visited = new Array();
    var result = [];
    var i, j;

    for (i = 0; i < m; i++) {
        visited[i] = [];
        for (j = 0; j < n; j++) {
            visited[i][j] = false;
        }
    }

    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            dfs(board, visited, i, j, tire, "", result);
        }
    }

    return result;
};

var dfs = function (board, visited, i, j, tire, str, result) {
    if (i < 0 || i >= board.length || j < 0 || j > board[0].length) {
        return;
    }

    if (visited[i][j]) {
        return;
    }

    str += board[i][j];
    if (!tire.startsWith(str)) {
        return;
    }

    if (tire.search(str)) {
        if (result.indexOf(str) < 0) {
            result.push(str.toString());
        }
    }

    visited[i][j] = true;
    dfs(board, visited, i+1, j, tire, str, result);
    dfs(board, visited, i-1, j, tire, str, result);
    dfs(board, visited, i, j+1, tire, str, result);
    dfs(board, visited, i, j-1, tire, str, result);
    visited[i][j] = false;
};

var TrieNode = function(key) {
    return {
        key: key,
        isWord: false
    };
};

var Trie = function() {
    this.root = TrieNode('root');
};

Trie.prototype.insert = function(word) {
    var tree = this.root, i, curr;
    for (i = 0; i < word.length; i++) {
        curr = word[i];
        if (!tree[curr]) {
            tree[curr] = new TrieNode(curr);
        }
        tree = tree[curr];
    }
    tree.isWord = true;
};

Trie.prototype.search = function(word) {
    var tree = this.root, i;
    for (i = 0; i < word.length; i++) {
        if (!tree[word[i]]) {
            return false;
        }
        tree = tree[word[i]];
    }

    return tree.isWord;
};

Trie.prototype.startsWith = function(prefix) {
    var tree = this.root, i;
    for (i = 0; i < prefix.length; i++) {
        if (!tree[prefix[i]]) {
            return false;
        }
        tree = tree[prefix[i]];
    }
    return true;
};