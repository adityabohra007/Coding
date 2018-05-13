"""
Given a string s, 
partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    def partition(self, s):
        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, path):
        if len(s) == 0:
            self.result.append(path)
            return
        for i in xrange(1, len(s) + 1):
            word = s[:i]
            if self.isPalindrome(word):
                self.dfs(s[i:], path + [s[:i]])

    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
