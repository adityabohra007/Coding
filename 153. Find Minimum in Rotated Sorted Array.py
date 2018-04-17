class Solution(object):
    def findMin(self, nums):
        if not nums or len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1
        target = nums[-1]

        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                high = mid
            else:
                low = mid

        return min(nums[low], nums[high])
