class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        x = m - 1
        y = 0

        while x >= 0 and y < n:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                return True
        return False