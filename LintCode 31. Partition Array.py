class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            while lo <= hi and nums[lo] < k:
                lo += 1
            while lo <= hi and nums[hi] >= k:
                hi -= 1
            if lo <= hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        return lo
