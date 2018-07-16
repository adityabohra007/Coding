class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None or len(A) == 0:
            return 0
        total = sum(A)
        initialSum = 0
        for i, v in enumerate(A):
            initialSum += i*v
        result = initialSum
        for i in xrange(len(A)-1, 0, -1):
            initialSum += total - len(A)*A[i]
            result = max(result, initialSum)
        return result
