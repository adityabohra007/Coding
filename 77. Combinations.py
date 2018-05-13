"""
Given two integers n and k, 
return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        self.result = []
        self.dfs(n, k, 1, [])
        return self.result

    def dfs(self, n, k, index, path):
        if len(path) == k:
            self.result.append(path[:])
            return
        for i in xrange(index, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, path)
            path.pop()