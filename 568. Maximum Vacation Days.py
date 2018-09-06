"""
非 dp 方法， 只能通过 71%
"""
class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        self.result = 0
        if len(flights) == 0 or len(days) == 0:
            return self.result
        self.helper(flights, days, 0, 0, 0)
        return self.result

    def helper(self, flights, days, city, cur_week, total):
        if cur_week == len(days):
            if total > self.result:
                self.result = total
            return
        for i in xrange(len(flights[city])):
            if (i == city or flights[city][i] == 1) and i < len(days) and cur_week < len(days[i]):
                self.helper(flights, days, i, cur_week + 1, total+days[i][cur_week])

"""
方法2： dp
起始状态为在最后一个week里面在每个city所能呆的最长时间
然后从后往前更新DP数组，需要考虑flights的限制
最后在第一天的DP数组里面，找出从city 0能到达的里面天数最大的即可
"""
class Solution2(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        m = len(days)
        n = len(days[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            dp[i][n-1] = days[i][n-1]
        
        for week in xrange(n-2, -1, -1):
            for city in xrange(m):
                dp[city][week] = days[city][week] + self.getMaxDays(dp, city, week+1, flights)
        
        return self.getMaxDays(dp, 0, 0, flights)
    
    def getMaxDays(self, dp, city, week, flights):
        maxDays = dp[city][week]
        for i in xrange(len(flights)):
            if flights[city][i] == 1:
                maxDays = max(maxDays, dp[i][week])
        return maxDays
        
