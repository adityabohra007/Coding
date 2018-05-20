"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. 
Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
"""
首先先去除wordList的重复值
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)

        wordLen = len(beginWord)
        from collections import deque
        q = deque([(beginWord, 1)])

        while q:
            curWord, step = q.popleft()
            if curWord == endWord:
                return step
            for i in xrange(wordLen):
                leftPart = curWord[:i]
                rightPart = curWord[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if curWord[i] != j:
                        nextWord = leftPart + j + rightPart
                        if nextWord in wordSet:
                            q.append((nextWord, step + 1))
                            wordSet.remove(nextWord)
        return 0