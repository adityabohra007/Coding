class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        node = self.root
        for letter in word:
            node = node.childs.get(letter)
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.childs.get(letter)
            if node is None:
                return False
        return True


class Solution(object):
    DIRECT_X = [1, 0, 0, -1]
    DIRECT_Y = [0, 1, -1, 0]

    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.result = {}
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                self.dfs(board, visited, i, j, trie, "")
        return self.result.keys()

    def dfs(self, board, visited, i, j, trie, s):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if visited[i][j]:
            return
        s += board[i][j]
        if trie.startsWith(s) == False:
            return
        if trie.search(s):
            self.result[s[:]] = True
        visited[i][j] = True
        for p in xrange(4):
            self.dfs(board, visited, i + self.DIRECT_X[p],
                     j + self.DIRECT_Y[p], trie, s)
        visited[i][j] = False

"""
Solution 2: 速度快了近一倍
flag: 单词的最后一个字母，是一个单词
hasWord：这个node包含大于等于一个的字母
pop()：每当找到一个单词，就重新整理一遍trie，清除掉那个找到的支线，如果这个node下面没有字母了，
hasword->false
"""


class Trie:
    def __init__(self):
        self.children = {}
        self.flag = False
        self.hasWord = False

    def put(self, key):
        if key == '':
            self.flag = True
            self.hasWord = True
            return

        if key[0] not in self.children:
            self.children[key[0]] = Trie()
        self.hasWord = True
        self.children[key[0]].put(key[1:])

    def pop(self, key):
        if key == '':
            self.flag = False
            self.hasWord = False
            return
        if key[0] not in self.children:
            return
        self.children[key[0]].pop(key[1:])
        self.hasWord = any([child.hasWord for child in self.children.values()])

    def has(self, key):
        if key == '':
            return self.flag

        if not self.hasWord:
            return False
        if key[0] not in self.children:
            return False
        return self.children[key[0]].has(key[1:])


class Solution(object):
    DIRECT_X = [1, 0, 0, -1]
    DIRECT_Y = [0, 1, -1, 0]

    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.put(word)

        self.results = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(trie, trie, board, r, c, [])
        return self.results.keys()

    def search(self, root, trie, board, x, y, chars):
        char = board[x][y]
        if char not in trie.children:
            return
        chars.append(char)
        trie = trie.children[char]
        if trie.flag:
            self.results[''.join(chars)] = True
            root.pop(''.join(chars))

        board[x][y] = '.'
        for i in range(4):
            r = x + self.DIRECT_X[i]
            c = y + self.DIRECT_Y[i]
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
                continue
            self.search(root, trie, board, r, c, chars)
        board[x][y] = char
        chars.pop()