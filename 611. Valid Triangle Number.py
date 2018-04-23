class Solution(object):
    def triangleNumber(self, nums):
        result = 0
        nums = sorted(nums, reverse=True)

        for i in xrange(len(nums) - 2):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                total = nums[lo] + nums[hi]
                if total > nums[i]:
                    result += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return result
