class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0]+'/'+nums[1]
        else:
            return nums[0]+'/('+'/'.join(nums[1:])+')'
