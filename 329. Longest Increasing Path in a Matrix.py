class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        res = 0
        n, m = len(matrix), len(matrix[0])

        # dp[i][j]表示从(i, j)点出发获得的Longest Increasing Path
        dp = [[0 for j in xrange(m)] for i in xrange(n)]

        for i in xrange(n):
            for j in xrange(m):
                res = max(res, self.dfs(matrix, Point(i, j), dp))
        return res

    def dfs(self, matrix, point, dp):
        n, m = len(matrix), len(matrix[0])

        if dp[point.x][point.y] != 0:
            return dp[point.x][point.y]

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x = point.x + dx
            y = point.y + dy

            if x < 0 or x >= n:
                continue

            if y < 0 or y >= m:
                continue

            if matrix[x][y] <= matrix[point.x][point.y]:
                continue

            # 从四周选一个最长的path
            dp[point.x][point.y] = max(
                dp[point.x][point.y], self.dfs(matrix, Point(x, y), dp))

        dp[point.x][point.y] += 1  # 再加上当前点

        return dp[point.x][point.y]
