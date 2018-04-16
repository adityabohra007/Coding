class Solution_1:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):
        map = {}
        length = len(nums)

        for i in xrange(length):
            map[nums[i]] = i

        if target in map:
            return map[target]
        else:
            return -1

"""
用二分法解题
"""
class Solution_2:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        
        if not nums or target is None:
            return -1
            
        l = 0
        h = len(nums) - 1
        
        while l + 1 < h:
            m = l + (h-l)/2
            if nums[m] <= target:
                l = m
            else:
                h = m
        
        if nums[h] == target:
            return h
        elif nums[l] == target:
            return l
        else:
            return -1