class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        result = []
        for i in xrange(len(nums)):
            result.append(p)
            p *= nums[i]
        p = 1
        for i in xrange(len(result) - 1, -1, -1):
            result[i] *= p
            p *= nums[i]
        return result
