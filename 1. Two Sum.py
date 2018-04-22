class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in xrange(len(nums)):
            map[nums[i]] = i

        for j in xrange(len(nums)):
            num = target - nums[j]
            if num in map and (num != nums[j] or map[num] != j):
                return [j, map[num]]
        return []
