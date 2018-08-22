# BFS
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        result = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "0":
                    self.count = 0
                    self.helper(grid, i, j, 'up')
                    self.helper(grid, i, j, 'down')
                    self.helper(grid, i, j, 'left')
                    self.helper(grid, i, j, 'right')
                    result = max(result, self.count)
        return result

    def helper(self, grid, i, j, d):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                self.count += 1
            if d == 'up':
                self.helper(grid, i-1, j, d)
            elif d == 'down':
                self.helper(grid, i+1, j, d)
            elif d == 'left':
                self.helper(grid, i, j-1, d)
            elif d == 'right':
                self.helper(grid, i, j+1, d)

# Solution2
class Solution2(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), 0
        if m:
            n = len(grid[0])
        result, rows = 0, 0
        cols = [0 for i in xrange(n)]
        
        for i in xrange(m):
            for j in xrange(n):
                if j == 0 or grid[i][j-1] == "W":
                    rows = 0
                    for k in xrange(j, n):
                        if grid[i][k] == "W":
                            break
                        if grid[i][k] == "E":
                            rows += 1
                
                if i == 0 or grid[i-1][j] == "W":
                    cols[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] == "W":
                            break
                        if grid[k][j] == "E":
                            cols[j] += 1
                if grid[i][j] == "0":
                    result = max(result, rows+cols[j])
        return result
