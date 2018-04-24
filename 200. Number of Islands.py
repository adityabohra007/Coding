class Solution_1(object):
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = [[False for i in xrange(n)] for i in xrange(m)]
        result = 0

        for i in xrange(m):
            for j in xrange(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    result += 1
                    self.bfs(grid, visited, i, j)

        return result

    def bfs(self, grid, visited, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(
                grid[0]) and visited[i][j] == False and grid[i][j] == '1':
            visited[i][j] = True
            self.bfs(grid, visited, i - 1, j)
            self.bfs(grid, visited, i + 1, j)
            self.bfs(grid, visited, i, j - 1)
            self.bfs(grid, visited, i, j + 1)

"""
Solution 2
"""


class Solution_2:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in xrange(n)] for i in xrange(m)]
        result = 0

        def checkPoint(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and visited[x][y] == False and grid[x][y]:
                return True
            return False

        def bfs(x, y):
            row = [1, 0, -1, 0]
            col = [0, 1, 0, -1]
            q = [(x, y)]
            while len(q) > 0:
                x = q[0][0]
                y = q[0][1]
                visited[x][y] = True
                q.pop(0)
                for k in xrange(4):
                    newX = x + row[k]
                    newY = y + col[k]
                    if checkPoint(newX, newY):
                        q.append((newX, newY))

        for i in xrange(m):
            for j in xrange(n):
                if checkPoint(i, j):
                    result += 1
                    bfs(i, j)
        return result