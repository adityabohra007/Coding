"""
https://segmentfault.com/a/1190000004878083
原理是这样的：
先对矩阵matrix的每个点到左顶点之间的子矩阵求和，存在新矩阵sum上。
注意，sum[i+1][j+1]代表的是matrix[0][0]到matrix[i][j]的子矩阵求和。如下所示：
Given matrix[m][n]
------------------
[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
Get sum[m+1][n+1]
-----------------
0  0  0  0
0  1  6  13
0  4  16 15
0  8  12 20

"""

class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):

        lenM = len(matrix)
        lenN = len(matrix[0])

        if lenM == lenN == 1 and matrix[0][0] == 0:
            return [[0, 0], [0, 0]]

        f = [[0 for x in xrange(lenN + 1)] for y in xrange(lenM + 1)]

        for i in xrange(1, lenM + 1):
            for j in xrange(1, lenN + 1):
                f[i][
                    j] = f[i][j - 1] + f[i - 1][j] - f[i -
                                                       1][j -
                                                          1] + matrix[i -
                                                                      1][j - 1]
                for m in xrange(i):
                    for n in xrange(j):
                        if f[i][j] == f[i][n] + f[m][j] - f[m][n]:
                            return [[m, n], [i - 1, j - 1]]
