class Solution(object):
    def maximumProduct(self, nums):
        nums = sorted(nums)
        
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
        
        