"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution(object):
    def totalNQueens(self, n):
        self.result = []
        self.dfs(n, [])
        return len(self.result)

    def dfs(self, n, tmp):
        if len(tmp) == n:
            self.result.append(tmp[:])
            return

        for i in xrange(n):
            if self.isValid(tmp, i):
                self.dfs(n, tmp + [i])

    def isValid(self, tmp, column):
        cur = len(tmp)
        for i in xrange(cur):
            if tmp[i] == column:
                return False
            if i + tmp[i] == cur + column:
                return False
            if i - tmp[i] == cur - column:
                return False
        return True