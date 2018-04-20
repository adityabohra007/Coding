"""
因为数组中数的范围是 [-10,000, 10,000], 所以我们所求的平均数也在这个范围内，一开始定lo=-10,000
hi=10,000, 所以中值是0
我们用二分搜索，
total[i]: 前i个数分别减去mid的值的总和
min_pre[i]: 前i个total值最小的那个
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        lo = -1e4
        hi = 1e4
        diff = 1e-5

        while lo + diff < hi:
            mid = (lo + hi) / 2
            if self.check(nums, k, mid):
                lo = mid
            else:
                hi = mid
        return lo

    def check(self, nums, k, mid):
        total = [0 for i in xrange(len(nums) + 1)]
        min_pre = [0 for i in xrange(len(nums) + 1)]

        for i in xrange(1, len(nums) + 1):
            total[i] = total[i - 1] + nums[i - 1] - mid
            min_pre[i] = min(min_pre[i - 1], total[i])

            if i >= k and total[i] - min_pre[i - k] >= 0:
                return True
        return False
