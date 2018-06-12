class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        result = [[0, 359, 1]]
        for i in xrange(1, n):
            index = 0
            for j in xrange(i):
                if result[j][1] - result[j][0] > result[index][1] - result[index][0]:
                    index = j
            x, y = result[index][0], result[index][1]
            result[index][1] = (x + y) / 2
            result.append([(x+y)/2+1, y, i+1])
        return result