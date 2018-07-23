class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return
        minS, result, sum = 0, nums[0], 0
        for num in nums:
            sum += num
            result = max(result, sum - minS)
            minS = min(minS, sum)
        return result
