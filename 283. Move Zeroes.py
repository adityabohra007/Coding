class Solution(object):
    def moveZeroes(self, nums):
        lo, hi = 0, 0

        while hi < len(nums):
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
            hi += 1
