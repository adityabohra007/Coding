/**
 实现字典树，每个节点至多有26个子孙，代表26个字母。

 每个节点都有三个属性，key, isWord以及字典(哈希表，提高访问速度，也可以用数组)，因为JS可以扩展实例化的对象，直接用下标访问对象，不需要再建一个哈希表了。

 root节点没有key和isWord，剩下的节点key记录该节点的值。

 isWord：比如单词为"tree"，"tre" -> 不是单词， "tree" -> 是单词。

 构造完字典后，比如要查找"tree"，只需要这样访问：root['t']['r']['e']['e'].isWord，任意一步拿不到就说明单词不在字典中。
 */
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