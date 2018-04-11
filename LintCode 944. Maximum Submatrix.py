class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """

    def maxSubmatrix(self, matrix):
        lenM = len(matrix)
        if lenM == 0:
            return 0
        lenN = len(matrix[0])
        if lenN == 0:
            return 0

        f = [[0 for x in xrange(lenN + 1)] for y in xrange(lenM + 1)]

        for i in xrange(1, lenM + 1):
            for j in xrange(1, lenN + 1):
                f[i][j] = f[i][j-1] + f[i-1][j] - f[i-1][j-1] + matrix[i-1][j-1]

        ans = -sys.maxint
        for low in xrange(lenM):
            for high in xrange(low + 1, lenM + 1):
                subsum = 0
                for k in range(1, lenN + 1):
                    diff = f[high][k] - f[low][k] - (
                        f[high][k - 1] - f[low][k - 1])
                    subsum += diff
                    ans = max(ans, subsum)
                    if subsum < 0:
                        subsum = 0

        return ans
