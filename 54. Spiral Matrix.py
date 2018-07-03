class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        px = [0, 1, 0, -1]
        py = [1, 0, -1, 0]
        m = len(matrix)
        n = len(matrix[0])
        used = [[0 for _ in xrange(n)] for _ in xrange(m)]
        result = []
        q = [(0, 0, 0, 1)]
        while q:
            last = q.pop()
            x = last[0]
            y = last[1]
            dx = last[2]
            dy = last[3]
            result.append(matrix[x][y])
            used[x][y] = 1
            newX = x + dx
            newY = y + dy
            if newX >= 0 and newX < m and newY >= 0 and newY < n and used[newX][newY] == 0:
                q.append((newX, newY, dx, dy))
            else:
                for i in xrange(4):
                    newX = x + px[i]
                    newY = y + py[i]
                    if newX >= 0 and newX < m and newY >= 0 and newY < n and used[newX][newY] == 0:
                        q.append((newX, newY, px[i], py[i]))
                        break
        return result

"""
Solution 2
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        up, left = 0, 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        d = 0 # 0: go right | 1: go down | 2: go left | 3: go up
        result = []
        while True:
            if d == 0:
                for i in xrange(left, right+1):
                    result.append(matrix[up][i])
                up += 1
            if d == 1:
                for i in xrange(up, down+1):
                    result.append(matrix[i][right])
                right -= 1
            if d == 2:
                for i in xrange(right, left-1, -1):
                    result.append(matrix[down][i])
                down -= 1
            if d == 3:
                for i in xrange(down, up-1, -1):
                    result.append(matrix[i][left])
                left += 1
            if left > right or up > down:
                return result
            d = (d + 1) % 4
            
                

