class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        result = [0, 0]
        nums = sorted(nums)
        for i in xrange(len(nums)):
            if i != 0 and nums[i]-nums[i-1] == 0:
                result[0] = nums[i]
            elif i != 0 and nums[i]-nums[i-1] == 2:
                result[1] = nums[i]-1
        if result[1] == 0:
            if nums[0] != 1:
                result[1] = 1
            else:
                result[1] = len(nums)
        return result
