"""
假设是一个3*4的矩阵，low = 0, high = 11, 那么mid = 5
5 = 4x + 1
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0 or len(
                matrix[0]) == 0 or target == None:
            return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low + 1 < high:
            mid = (low + high) / 2
            x, y = mid / n, mid % n
            if matrix[x][y] < target:
                low = mid
            else:
                high = mid

        x, y = low / n, low % n
        if matrix[x][y] == target:
            return True

        x, y = high / n, high % n
        if matrix[x][y] == target:
            return True

        return False
