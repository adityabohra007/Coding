class Solution(object):
    def wordSquares(self, words):
        self.result = []
        l = len(words)
        if l == 0:
            return self.result
        trie = self.buildTrie(words)
        self.dfs(trie, [], 0, len(words[0]), "")
        return self.result

    def dfs(self, trie, item, chari, wordLength, prefix):
        cands = self.getWords(trie, prefix)
        for cand in cands:
            if len(item) == wordLength - 1:
                self.result.append(list(item + [cand]))
                continue
            newPrefix = ''.join([word[chari + 1] for word in (item + [cand])])
            self.dfs(trie, item + [cand], chari + 1, wordLength, newPrefix)

    def getWords(self, trie, prefix):
        for c in prefix:
            if c not in trie:
                return []
            trie = trie[c]
        res = []
        self.collectTrie(trie, res, prefix)
        return res

    def collectTrie(self, trie, res, prefix):
        if not trie:
            if len(prefix) > 0:
                res.append(prefix)
            return

        for c in trie:
            self.collectTrie(trie[c], res, prefix + c)

    def buildTrie(self, words):
        trie = {}
        for word in words:
            self.addWord(trie, word, 0)
        return trie

    def addWord(self, trie, word, startIndex):
        if startIndex == len(word):
            return
        if word[startIndex] not in trie:
            trie[word[startIndex]] = {}
        self.addWord(trie[word[startIndex]], word, startIndex + 1)
