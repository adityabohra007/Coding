import sys


class Solution(object):
    def maxProfit(self, prices):
        diff = 0
        low = sys.maxint

        for price in prices:
            if price - low > diff:
                diff = price - low
            if price < low:
                low = price

        return diff
