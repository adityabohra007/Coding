from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or len(heightMap) == 0:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        offset = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = [[0 for _ in xrange(n)] for _ in xrange(m)]
        heap = []
        for i in xrange(m):
            heappush(heap, (heightMap[i][0], i, 0))
            visited[i][0] = 1
            heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][n-1] = 1
        for i in xrange(n):
            heappush(heap, (heightMap[0][i], 0, i))
            visited[0][i] = 1
            heappush(heap, (heightMap[m-1][i], m-1, i))
            visited[m-1][i] = 1
        
        result = 0
        while heap:
            h, x, y = heappop(heap)
            for dx, dy in offset:
                newX = x + dx
                newY = y + dy
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY]:
                    visited[newX][newY] = 1
                    newH = max(h, heightMap[newX][newY])
                    heappush(heap, (newH, newX, newY))
                    if h > heightMap[newX][newY]:
                        result += h - heightMap[newX][newY]
        return result
        