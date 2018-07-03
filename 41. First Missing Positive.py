class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 1
        n = len(nums)
        i = 0
        while i < n:
            w = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[w]:
                nums[i], nums[w] = nums[w], nums[i]
            else:
                i += 1
        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
