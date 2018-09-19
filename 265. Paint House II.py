import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        r1, r2, p = 0, 0, -1
        for i in xrange(n):
            t1, t2, tp = sys.maxint, sys.maxint, -1
            for j in xrange(k):
                total = r1 + costs[i][j] if j != p else r2 + costs[i][j]
                if total <= t1:
                    t1, t2, tp = total, t1, j
                elif total <= t2:
                    t2 = total
            r1, r2, p = t1, t2, tp
        return r1