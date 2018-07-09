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

"""
Solution 2
"""
class Solution2(object):
    def maxProfit(self, prices):
        result = 0
        if len(prices) == 0:
            return result
        minP = prices[0]
        
        for price in prices:
            result = max(result, price - minP)
            minP = min(minP, price)
        return result
        
