class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxP = [i for i in nums]
        minP = [i for i in nums]
        for i in xrange(1, len(nums)):
            res = [maxP[i-1]*nums[i], minP[i-1]*nums[i], nums[i]]
            maxP[i] = max(res)
            minP[i] = min(res)
        return max(maxP)
