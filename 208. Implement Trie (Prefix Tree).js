var TrieNode = function(key) {
    return {
        key: key,
        isWord: false
    };
};
/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.root = TrieNode('root');
};

/**
 * Inserts a word into the trie.
 * @param {string} word
 * @return {void}
 */
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

/**
 * Returns if the word is in the trie.
 * @param {string} word
 * @return {boolean}
 */
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

/**
 * Returns if there is any word in the trie that starts with the given prefix.
 * @param {string} prefix
 * @return {boolean}
 */
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

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Object.create(Trie).createNew()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */