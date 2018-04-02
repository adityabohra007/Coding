class Solution(object):
    def multiply(self, A, B):

        n = len(A)
        m = len(A[0])
        k = len(B[0])

        C = [[0 for i in xrange(k)] for i in xrange(n)]

        for i in xrange(n):
            for j in xrange(m):
                if A[i][j] != 0:
                    for l in xrange(k):
                        C[i][l] += A[i][j] * B[j][l]
        return C
