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