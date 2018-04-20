class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        if not nums or len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return -1

        low = 0
        high = len(nums) - 1

        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid

        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        else:
            return -1