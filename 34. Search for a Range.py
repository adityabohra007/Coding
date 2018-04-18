class Solution(object):
    def searchRange(self, nums, target):
        result = [-1, -1]
        if not nums or len(nums) == 0 or target is None:
            return result

        low, high = 0, len(nums) - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid

        if nums[low] == target:
            result[0] = low
        elif nums[high] == target:
            result[0] = high
        else:
            return result

        low, high = 0, len(nums) - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid

        if nums[high] == target:
            result[1] = high
        elif nums[low] == target:
            result[1] = low

        return result
