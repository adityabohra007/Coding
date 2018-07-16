class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        if len(M) == 0 or len(M[0]) == 0:
            return result
        m = len(M)
        n = len(M[0])
        result = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                sum = 0
                count = 0
                for x in xrange(max(0, i-1), min(i+2, m)):
                    for y in xrange(max(0, j-1), min(j+2, n)):
                        sum += M[x][y]
                        count += 1
                result[i][j] = sum/count
        return result
