class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if m == 0:
            return
        n = len(dungeon[0])
        if n == 0:
            return
        dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
        dp[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)
        for i in xrange(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for i in xrange(n - 2, -1, -1):
            dp[m - 1][i] = max(dp[m - 1][i + 1] - dungeon[m - 1][i], 1)
        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                cur = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(cur - dungeon[i][j], 1)
        return dp[0][0]
