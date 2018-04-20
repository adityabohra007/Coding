class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums) == 0 or target is None:
            return False

        lo = 0
        hi = len(nums) - 1

        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[hi]:
                hi -= 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[lo] <= target and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        if nums[lo] == target:
            return True
        elif nums[hi] == target:
            return True
        else:
            return False
