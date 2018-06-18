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

"""
Solution 2
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left+right)/2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            start = left
        elif nums[right] == target:
            start = right
        else:
            return [-1, -1]
        l = 0
        for num in nums[start:]:
            if num == target:
                l += 1
            else:
                break
        return [start, start+l-1]
                
