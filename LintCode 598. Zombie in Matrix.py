class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1

        q = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]
        result = 0

        while q:
            result += 1
            for k in xrange(len(q)):
                point = q.pop(0)
                x = point[0]
                y = point[1]
                for i in xrange(len(row)):
                    newX = x + row[i]
                    newY = y + col[i]
                    if newX >= 0 and newX < m and newY >= 0 and newY < n and grid[newX][newY] == 0:
                        q.append((newX, newY))
                        grid[newX][newY] = 1

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    return -1

        return result - 1
