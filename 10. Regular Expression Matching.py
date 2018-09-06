class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    hash = {}
    def isMatch(self, s, p):
        # write your code here
        if self.hash is None:
            self.hash = {}
        key = s + p
        if key in self.hash:
            return self.hash[key]
        if len(p) == 0:
            return len(s) == 0
        if len(s) == 0:
            if len(p) == 0 or len(p) % 2 == 1:
                return False
            i = 1
            while i < len(p):
                if p[i] != '*':
                    return False
                i += 2
            return True
        
        if len(p) > 1 and p[1] == '*':
            if p[0] == '.':
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            elif s[0] == p[0]:
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                self.hash[key] = self.isMatch(s, p[2:]) 
        elif p[0] == '.':
            self.hash[key] = self.isMatch(s[1:], p[1:])
        else:
            self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])
        
        return self.hash[key]

"""
方法2：DP
"""
class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in xrange(len(p)+1)] for _ in xrange(len(s)+1)]
        dp[0][0] = True
        for j in xrange(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
                else:
                    if s[i-1] == p[j-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
        return dp[len(s)][len(p)]
        