class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        elif (len(nums) == 1):
            return nums[0]
        else:
            dp = [0]*(len(nums)+2)
            for i in range(2,len(nums)+2):
                dp[i] = max(dp[i-2]+nums[i-2],dp[i-1])
        return dp[len(nums)+1]
        