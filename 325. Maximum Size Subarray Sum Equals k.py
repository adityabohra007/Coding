class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        if nums is None or len(nums) == 0:
            return result
        hash = {}
        hash[0] = 0
        total = 0
        for i in xrange(len(nums)):
            total += nums[i]
            target = total - k
            if target in hash:
                result = max(result, i+1-hash[target])
            if total not in hash:
                hash[total] = i+1
        return result
