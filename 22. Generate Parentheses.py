"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):
    def generateParenthesis(self, n):
        self.result = []
        self.dfs(n, "", 0, 0)
        return self.result

    def dfs(self, n, tmp, index, total):
        if index == n and total == 0:
            self.result.append(tmp)
            return
        for p in ['(', ')']:
            if p == '(' and index < n:
                self.dfs(n, tmp + '(', index + 1, total + 1)
            elif p == ')' and total > 0:
                self.dfs(n, tmp + ')', index, total - 1)
