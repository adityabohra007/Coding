"""
Given two words (beginWord and endWord), 
and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
"""
会出现编码错误，在lintcode上可以运行
"""
class Solution(object):
    Graph = {}
    result = []
    visited = set()

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return self.result
        self.Graph[beginWord] = set()
        self.Graph[endWord] = set()
        for word in wordList:
            self.Graph[word] = set()

        self.buildGraph(beginWord, wordList)
        self.buildGraph(endWord, wordList)
        for word in wordList:
            self.buildGraph(word, wordList)

        dists = self.bfs(endWord)
        self.dfs(beginWord, endWord, [], dists)
        return self.result

    def buildGraph(self, word, dict):
        for i in xrange(len(word)):
            l = word[:i]
            r = word[i + 1:]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] != c:
                    curWord = l + c + r
                    if curWord in dict:
                        self.Graph[word].add(curWord)
                        self.Graph[curWord].add(word)

    def bfs(self, end):
        queue = []
        dists = {}
        queue.append(end)
        dists[end] = 0
        self.visited.add(end)

        while queue:
            cur = queue.pop(0)
            for child in self.Graph[cur]:
                if child not in self.visited:
                    queue.append(child)
                    self.visited.add(child)
                    dists[child] = dists[cur] + 1
        return dists

    def dfs(self, start, end, tmp, dists):
        tmp.append(start)
        if start == end:
            self.result.append(tmp[:])
            return

        for child in self.Graph[start]:
            if dists[child] != dists[start] - 1:
                continue
            self.dfs(child, end, tmp, dists)
            tmp.pop()