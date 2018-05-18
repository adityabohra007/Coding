"""
Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def permuteUnique(self, nums):
        self.result = []
        nums = sorted(nums)
        used = [False] * len(nums)
        self.dfs(nums, used, [])
        return self.result

    def dfs(self, nums, used, tmp):
        if len(tmp) == len(nums):
            self.result.append(tmp[:])
            return

        for i in xrange(len(nums)):
            if used[i] == False and (i == 0 or nums[i] != nums[i - 1]
                                     or used[i - 1] == True):
                used[i] = True
                self.dfs(nums, used, tmp + [nums[i]])
                used[i] = False
