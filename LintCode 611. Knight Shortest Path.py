"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m = len(grid)
        n = len(grid[0])
        row = [1, 1, -1, -1, 2, 2, -2, -2]
        col = [2, -2, 2, -2, 1, -1, 1, -1]

        result = -1
        import Queue
        q = Queue.Queue(maxsize=m * n)
        q.put(source)

        while not q.empty():
            result += 1
            for i in xrange(q.qsize()):
                point = q.get()
                if point.x == destination.x and point.y == destination.y:
                    return result
                for i in xrange(len(row)):
                    newX = point.x + row[i]
                    newY = point.y + col[i]
                    if newX >= 0 and newX < m and newY >= 0 and newY < n and grid[newX][newY] != 1:
                        grid[newX][newY] = 1
                        q.put(Point(newX, newY))
        return -1
