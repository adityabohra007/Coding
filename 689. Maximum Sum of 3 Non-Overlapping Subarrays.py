"""
算出从左到右的左侧最大值 和从右到左的左侧最大值
枚举中间的subarray 根据已经算好的两个最大值可以立刻知道每个中间subarray的最大3sum
每个中间subarray的最大3sum打擂台
"""
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums is None or len(nums) < k:
            return []
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in xrange(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        posLeft = [0] * n
        posRight = [0] * n

        # posLeft[i]: 以i为右边界的满足长度k的最大值得起始点
        max_sum = prefix_sum[k] - prefix_sum[0]
        for i in xrange(k, n):
            if prefix_sum[i + 1] - prefix_sum[i - k + 1] > max_sum:
                max_sum = prefix_sum[i + 1] - prefix_sum[i - k + 1]
                posLeft[i] = i - k + 1
            else:
                posLeft[i] = posLeft[i - 1]

        # posRight[i]: 以i为左边界的满足长度k的最大值得起始点 
        posRight[n - k] = n - k
        max_sum = prefix_sum[n] - prefix_sum[n - k]
        for i in xrange(n - k - 1, -1, -1):
            if prefix_sum[i + k] - prefix_sum[i] > max_sum:
                max_sum = prefix_sum[i + k] - prefix_sum[i]
                posRight[i] = i
            else:
                posRight[i] = posRight[i + 1]

        # test all middle interval
        max_sum = 0
        result = [0, 0, 0]
        for i in xrange(k, n - 2 * k + 1):
            l = posLeft[i - 1]
            r = posRight[i + k]
            total = (prefix_sum[i + k] - prefix_sum[i]) + (prefix_sum[l + k] - prefix_sum[l]) + (
                        prefix_sum[r + k] - prefix_sum[r])
            if total > max_sum:
                max_sum = total
                result = [l, i, r]
        return result


