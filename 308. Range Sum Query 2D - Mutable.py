"""
非 binary indexed tree 方法
"""
class NumMatrix_1(object):

    def __init__(self, matrix):
        lenM = len(matrix)
        if lenM == 0:
            return
        lenN = len(matrix[0])
        if lenN == 0:
            return

        self.m = matrix
        self.f = [[0 for x in xrange(lenN+1)] for y in xrange(lenM+1)]
        for i in xrange(1, lenM+1):
            for j in xrange(1, lenN+1):
                self.f[i][j] = self.f[i-1][j] + self.f[i][j-1] - self.f[i-1][j-1] + matrix[i-1][j-1]


    def update(self, row, col, val):
        lenM = len(self.f)
        lenN = len(self.f[0])
        for i in xrange(row+1, lenM):
            for j in xrange(col+1, lenN):
                self.f[i][j] += val-self.m[row][col]
        self.m[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):

        return self.f[row2+1][col2+1] - self.f[row1][col2+1] - self.f[row2+1][col1] + self.f[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

"""
binary index tree 方法
"""


class NumMatrix_2(object):
    def __init__(self, matrix):
        self.lenM = len(matrix)
        if self.lenM == 0:
            return
        self.lenN = len(matrix[0])
        if self.lenN == 0:
            return

        self.arr = [[0 for x in xrange(self.lenN)] for y in xrange(self.lenM)]
        self.btree = [[0 for x in xrange(self.lenN + 1)]
                      for y in xrange(self.lenM + 1)]

        for i in xrange(self.lenM):
            for j in xrange(self.lenN):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        diff = val - self.arr[row][col]
        self.arr[row][col] = val

        x = row + 1
        y = col + 1

        while x <= self.lenM:
            while y <= self.lenN:
                self.btree[x][y] += diff
                y += self.lowbit(y)
            x += self.lowbit(x)
            y = col + 1

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

    def lowbit(self, x):
        return x & -x


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)