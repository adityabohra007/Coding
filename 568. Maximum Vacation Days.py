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
