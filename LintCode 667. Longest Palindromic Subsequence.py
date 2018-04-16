"""
LintCode 516. Longest Palindromic Subsequence
"""
"""
这道题给了我们一个字符串，让我们求最大的回文子序列，子序列和子字符串不同，不需要连续。
而关于回文串的题之前也做了不少，处理方法上就是老老实实的两两比较吧。像这种有关极值的问题，
最应该优先考虑的就是贪婪算法和动态规划，这道题显然使用DP更加合适。
我们建立一个二维的DP数组，其中dp[i][j]表示[i,j]区间内的字符串的最长回文子序列，
那么对于递推公式我们分析一下，如果s[i]==s[j]，那么i和j就可以增加2个回文串的长度，
我们知道中间dp[i + 1][j - 1]的值，那么其加上2就是dp[i][j]的值。
如果s[i] != s[j]，那么我们可以去掉i或j其中的一个字符，然后比较两种情况下所剩的字符串谁dp值大，
就赋给dp[i][j]，那么递推公式如下：

            /  dp[i + 1][j - 1] + 2              if (s[i] == s[j])
dp[i][j] =
            \  max(dp[i + 1][j], dp[i][j - 1])   if (s[i] != s[j])
"""
class Solution_1:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        length = len(s)
        if length == 0:
            return 0

        dp = [[0 for _ in xrange(length)] for _ in xrange(length)]

        for i in xrange(length-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][length-1]

"""
Solution 2: 用一维数组
"""


class Solution_2(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [1] * n
        for j in xrange(1, len(s)):
            pre = dp[j]
            for i in reversed(xrange(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]
