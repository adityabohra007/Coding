class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if nums is None or len(nums) == 0:
            return result
        for i in xrange(len(nums)):
            if nums[i] != nums[result]:
                result += 1
                nums[result] = nums[i]
        return result + 1
