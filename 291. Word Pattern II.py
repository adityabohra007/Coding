"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, 
such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
"""
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        return self.dfs(pattern, str, [], {})

    def dfs(self, pattern, str, s, m):
        if len(pattern) == 0:
            return len(str) == 0

        char = pattern[0]
        if char in m:
            if str.startswith(m[char]) == False:
                return False
            return self.dfs(pattern[1:], str[len(m[char]):], s, m)

        for i in xrange(len(str)):
            word = str[:i + 1]
            if word in s:
                continue
            m[char] = word
            if self.dfs(pattern[1:], str[i + 1:], s + [word], m):
                return True
            del (m[char])
        return False