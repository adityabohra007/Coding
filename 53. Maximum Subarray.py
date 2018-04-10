import sys


class Solution(object):
    def maxSubArray(self, nums):
        maxSum = -sys.maxint - 1
        sum = 0
        minSum = 0

        for num in nums:
            sum += num
            maxSum = max(maxSum, sum - minSum)
            minSum = min(minSum, sum)

        return maxSum