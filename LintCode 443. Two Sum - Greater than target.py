class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums, target):
        lo, hi = 0, len(nums) - 1
        result = 0
        nums = sorted(nums)

        while lo < hi:
            total = nums[lo] + nums[hi]
            if total > target:
                result += hi - lo
                hi -= 1
            else:
                lo += 1
        return result
