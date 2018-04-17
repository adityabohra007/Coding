"""
只要找到其中一个高峰，不需要是最高的
"""



class Solution(object):
    def findPeakElement(self, nums):
        if not nums or len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1

        while low + 1 < high:
            mid = (low + high) / 2

            if nums[mid] < nums[mid + 1]:
                low = mid
            else:
                high = mid

        if nums[low] < nums[high]:
            return high
        else:
            return low
