class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        for i in xrange(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                total = nums[lo] + nums[hi]
                if total == target:
                    result.append([nums[i], nums[lo], nums[hi]])
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
