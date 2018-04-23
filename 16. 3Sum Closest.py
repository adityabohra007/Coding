class Solution(object):
    def threeSumClosest(self, nums, target):
        result = None
        import sys
        diff = sys.maxint
        nums = sorted(nums)

        for i in xrange(len(nums) - 2):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                total = nums[lo] + nums[hi] + nums[i]
                if result is None or abs(total - target) < diff:
                    result = total
                    diff = abs(total - target)
                if total == target:
                    return target
                elif total > target:
                    hi -= 1
                else:
                    lo += 1
        return result
