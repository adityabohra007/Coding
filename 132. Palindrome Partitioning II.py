"""
动态规划题
"""
import sys
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        n = len(s)
        dp = [i - 1 for i in range(n + 1)]
        for i in xrange(1, n+1):
            for j in xrange(i):
                if self.isPalindrome(s[j:i]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    def isPalindrome(self, c):
        low = 0
        high = len(c) - 1
        while low < high:
            if c[low] != c[high]:
                return False
            low += 1
            high -= 1
        return True