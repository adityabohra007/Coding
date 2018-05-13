"""
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        self.result = []
        nums = sorted(nums)
        from collections import defaultdict
        used = defaultdict(bool)
        self.dfs(nums, [], 0, used)
        return self.result

    def dfs(self, nums, tmp, index, used):
        self.result.append(tmp[:])
        for i in xrange(index, len(nums)):
            if i == 0 or nums[i] != nums[i - 1] or used[i - 1]:
                tmp.append(nums[i])
                used[i] = True
                self.dfs(nums, tmp, i + 1, used)
                tmp.pop()
                used[i] = False