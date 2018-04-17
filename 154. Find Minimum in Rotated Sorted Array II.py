class Solution(object):
    def findMin(self, nums):
        if not nums or len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1

        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid
            else:
                high -= 1

        return min(nums[low], nums[high])
