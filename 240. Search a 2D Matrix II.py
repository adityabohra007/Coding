class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        n = len(matrix)
        m = len(matrix[0])

        x = n - 1
        y = 0
        count = 0

        while x >= 0 and y < m:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                count += 1
                x -= 1
                y += 1

        return True if count > 0 else False