"""
分2段讨论
"""
class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums) == 0 or target is None:
            return -1

        low = 0
        high = len(nums) - 1

        while low + 1 < high:
            mid = (low + high) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[high]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] > target and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        else:
            return -1
