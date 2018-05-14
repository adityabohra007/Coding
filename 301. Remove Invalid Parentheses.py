"""
Remove the minimum number of invalid parentheses 
in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        self.result = []
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            if char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        self.dfs(s, left, right, 0)
        return self.result

    def dfs(self, s, left, right, index):
        if left == 0 and right == 0:
            if self.isValid(s):
                self.result.append(s)
            return
        for i in xrange(index, len(s)):
            if i != index and s[i] == s[i - 1]:
                continue
            if s[i] == '(':
                if left > 0:
                    subString = s[0:i] + s[i + 1:]
                    self.dfs(subString, left - 1, right, i)
            if s[i] == ')':
                if right > 0:
                    subString = s[0:i] + s[i + 1:]
                    self.dfs(subString, left, right - 1, i)

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
