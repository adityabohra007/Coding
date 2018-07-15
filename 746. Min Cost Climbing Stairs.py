class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)
        if l < 2:
            return 0
        dp = [0] * (l+1)
        for i in xrange(2, len(dp)):
            dp[i] = min((dp[i-2]+cost[i-2]), (dp[i-1]+cost[i-1]))
        return dp[-1]
