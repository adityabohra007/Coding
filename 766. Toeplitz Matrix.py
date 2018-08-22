class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return True
        n = len(matrix[0])
        if n == 0:
            return True
        for i in xrange(n):
            if self.check(matrix, 0, i, matrix[0][i]) == False:
                return False

        for j in xrange(1, m):
            if self.check(matrix, j, 0, matrix[j][0]) == False:
                return False
        return True

    def check(self, matrix, x, y, target):
        while x < len(matrix) and y < len(matrix[0]):
            if matrix[x][y] != target:
                return False
            x += 1
            y += 1
        return True
