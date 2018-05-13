"""
Given a set of distinct integers, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
class Solution(object):
    def subsets(self, nums):
        self.result = []
        nums = sorted(nums)
        self.dfs(nums, [], 0)
        return self.result

    def dfs(self, nums, tmp, index):
        self.result.append(tmp[:])
        for i in xrange(index, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, tmp, i + 1)
            tmp.pop()
