"""
LintCode上通过
LeetCode会 Memory Limit Exceeded
"""
class Solution(object):
    def __init__(self):
        self.hash = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        key = (s, p)
        if key in self.hash:
            return self.hash[key]
        if len(p) == 0:
            return len(s) == 0
        if len(s) == 0:
            if len(p) == 0:
                return True
            i = 0
            while i < len(p):
                if p[i] != '*':
                    return False
                i += 1
            return True
        if len(p) > 0 and p[0] == '*':
            self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        elif len(p) > 0 and p[0] == '?':
            self.hash[key] = self.isMatch(s[1:], p[1:])
        else:
            self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])
        return self.hash[key]


"""
Solution 2
"""


class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_match_helper(s, 0, p, 0, {})

    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # source is empty
        if len(source) == i:
            # every character should be "*"
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False
            return True

        if len(pattern) == j:
            return False

        if pattern[j] != '*':
            matched = self.is_match_char(source[i], pattern[j]) and \
                      self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        else:
            matched = self.is_match_helper(source, i + 1, pattern, j, memo) or \
                      self.is_match_helper(source, i, pattern, j + 1, memo)

        memo[(i, j)] = matched
        return matched

    def is_match_char(self, s, p):
        return s == p or p == '?'


