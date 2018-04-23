class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        nums = sorted(nums)
        result = 0

        while lo < hi:
            total = nums[lo] + nums[hi]
            if total == target:
                result += 1
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif total < target:
                lo += 1
            else:
                hi -= 1
        return result
