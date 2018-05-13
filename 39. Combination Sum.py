"""
Given a set of candidate numbers (candidates) 
(without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        self.result = []
        nums = sorted(candidates)
        self.dfs(nums, target, [], 0, 0)
        return self.result

    def dfs(self, nums, target, tmp, index, total):
        if total == target:
            self.result.append(tmp[:])
        for i in xrange(index, len(nums)):
            if total + nums[i] <= target:
                tmp.append(nums[i])
                self.dfs(nums, target, tmp, i, total + nums[i])
                tmp.pop()
