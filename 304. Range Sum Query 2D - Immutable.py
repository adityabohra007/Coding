class NumMatrix(object):

    def __init__(self, matrix):
        lenM = len(matrix)
        if lenM == 0:
            return
        lenN = len(matrix[0])
        if lenN == 0:
            return

        self.f = [[0 for x in xrange(lenN+1)] for y in xrange(lenM+1)]
        for i in xrange(1, lenM+1):
            for j in xrange(1, lenN+1):
                self.f[i][j] = self.f[i-1][j] + self.f[i][j-1] - self.f[i-1][j-1] + matrix[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        if row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0 or row1 > row2 or col1 > col2:
            return 0

        return self.f[row2+1][col2+1] - self.f[row1][col2+1] - self.f[row2+1][col1] + self.f[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

"""
binary index tree 方法
"""


class NumMatrix(object):
    def __init__(self, matrix):
        self.m = len(matrix)
        if self.m == 0:
            return
        self.n = len(matrix[0])
        if self.n == 0:
            return

        self.arr = matrix
        self.btree = [[0 for _ in xrange(self.n + 1)]
                      for _ in xrange(self.m + 1)]

        for i in xrange(self.m):
            for j in xrange(self.n):
                self.update(i, j)

    def sumRegion(self, row1, col1, row2, col2):
        return (self.prefixSum(row2, col2) - self.prefixSum(row2, col1 - 1) -
                self.prefixSum(row1 - 1, col2) +
                self.prefixSum(row1 - 1, col1 - 1))

    def prefixSum(self, row, col):
        sum = 0
        x = row + 1
        y = col + 1
        while x > 0:
            while y > 0:
                sum += self.btree[x][y]
                y -= self.lowbit(y)
            x -= self.lowbit(x)
            y = col + 1
        return sum

    def update(self, row, col):
        x = row + 1
        y = col + 1

        while x <= self.m:
            while y <= self.n:
                self.btree[x][y] += self.arr[row][col]
                y += self.lowbit(y)
            x += self.lowbit(x)
            y = col + 1

    def lowbit(self, x):
        return x & -x


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)