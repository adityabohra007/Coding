class Solution_1:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        nums = sorted(nums)
        result = 0
        for lo in xrange(len(nums) - 1):
            hi = len(nums) - 1
            while lo < hi:
                total = nums[lo] + nums[hi]
                if total <= target:
                    result += hi - lo
                    break
                hi -= 1
        return result

"""
双指针 更好的解决方法
"""


class Solution_2:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        nums = sorted(nums)
        result = 0
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            total = nums[lo] + nums[hi]
            if total <= target:
                result += hi - lo
                lo += 1
            else:
                hi -= 1
        return result
