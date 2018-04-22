class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        lo, hi = 0, 0
        map = {}
        result = 0

        while hi < len(nums):
            if nums[hi] not in map:
                map[nums[hi]] = True
                result += 1
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
            hi += 1

        return result