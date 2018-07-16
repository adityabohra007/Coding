"""
s:    "bbbab"
dp:   [4,3,3,1,1]
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        dp = [1] * len(s)
        for i in xrange(1, len(s)):
            pre = dp[i]
            for j in reversed(xrange(i)):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2 if j+1 <= i-1 else 2
                else:
                    dp[j] = max(dp[j], dp[j+1])
                pre = tmp
        return dp[0]
