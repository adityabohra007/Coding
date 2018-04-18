class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        if not nums or len(nums) == 0 or target is None:
            return -1

        low, high = 0, len(nums) - 1

        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid

        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        return -1
