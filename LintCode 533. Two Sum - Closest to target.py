class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        import sys
        result = sys.maxint

        nums = sorted(nums)

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            total = nums[lo] + nums[hi]
            if total == target:
                return 0
            elif total < target:
                lo += 1
            else:
                hi -= 1
            result = min(result, abs(total - target))

        return result
