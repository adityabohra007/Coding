class Solution(object):
    def fourSum(self, nums, target):
        nums = sorted(nums)
        result = []
        for i in xrange(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo = j + 1
                hi = len(nums) - 1
                while lo < hi:
                    total = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if total == target:
                        result.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    elif total < target:
                        lo += 1
                    else:
                        hi -= 1
        return result
