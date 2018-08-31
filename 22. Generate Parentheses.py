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
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.dfs('', n, 0, 0)
        return self.result
    
    def dfs(self, tmp, n, i, total):
        if i == n and total == 0:
            self.result.append(tmp[:])
            return
        for c in ['(', ')']:
            if c == '(' and i < n:
                self.dfs(tmp+c, n, i+1, total+1)
            if c == ')' and total > 0:
                self.dfs(tmp+c, n, i, total-1)

# Solution 2
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        if n < 0:
            return self.result
        self.helper(n, 0, 0, "")
        return self.result
    
    def helper(self, n, total, cur, tmp):
        if total == n and cur == 0:
            self.result.append(tmp)
            return
        if total > n:
            return
        if cur > 0:
            self.helper(n, total+1, cur+1, tmp+'(' )
            self.helper(n, total, cur-1, tmp+')' )
        elif cur == 0:
            self.helper(n, total+1, cur+1, tmp+'(' )
            
        
        
