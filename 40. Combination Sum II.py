"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        self.result = []
        num = sorted(candidates)
        from collections import defaultdict
        used = defaultdict(bool)
        self.dfs(num, target, [], 0, 0, used)
        return self.result

    def dfs(self, num, target, path, index, total, used):
        if total == target:
            self.result.append(path[:])
            return
        for i in xrange(index, len(num)):
            if total + num[i] <= target and (i == 0 or num[i] != num[i - 1]
                                             or used[i - 1]):
                path.append(num[i])
                used[i] = True
                self.dfs(num, target, path, i + 1, total + num[i], used)
                path.pop()
                used[i] = False
