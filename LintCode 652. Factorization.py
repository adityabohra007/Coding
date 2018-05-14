"""
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.

Example

Given n = 8
return [[2,2,2],[2,4]]
// 8 = 2 x 2 x 2 = 2 x 4.

Given n = 1
return []

Given n = 12
return [[2,6],[2,2,3],[3,4]]
"""
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        self.result = []
        self.dfs(n, [], 2)
        return self.result

    def dfs(self, n, tmp, index):
        if n == 1:
            if len(tmp) > 1:
                self.result.append(tmp[:])
            return

        import math
        for i in xrange(index, int(math.sqrt(n)) + 1):
            if n % i == 0:
                self.dfs(n / i, tmp + [i], i)
        if n >= index:
            self.dfs(1, tmp + [n], n)
