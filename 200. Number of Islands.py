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
class Solution2:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        result = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    result += 1
                    q = [(i, j)]
                    while q:
                        x, y = q.pop(0)
                        grid[x][y] = 2
                        for k in xrange(4):
                            newX = x + dx[k]
                            newY = y + dy[k]
                            if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and grid[newX][newY] == 1:
                                q.append((newX, newY))
        return result