"""
方法1：dp
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i, v in enumerate(nums):
            for j in xrange(i):
                if nums[j] < v:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

"""
方法2: 二分法 binary search
"""
import bisect
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        s = [nums[0]]
        for num in nums[1:]:
            if num > s[-1]:
                s.append(num)
            else:
                s[bisect.bisect_left(s, num)] = num
        return len(s)
        
        
