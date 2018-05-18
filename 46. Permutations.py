"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
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
            if used[i] == False:
                used[i] = True
                self.dfs(nums, used, tmp + [nums[i]])
                used[i] = False