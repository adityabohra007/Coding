class Solution(object):
    def setZeroes(self, matrix):
        if len(matrix) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])

        row = [False for i in xrange(m)]
        col = [False for i in xrange(n)]

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in xrange(m):
            for j in xrange(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
