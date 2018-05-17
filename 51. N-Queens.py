"""
The n-queens puzzle is the problem of placing n queens on 
an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
class Solution(object):
    def solveNQueens(self, n):
        self.result = []
        self.dfs(n, [])
        return self.result

    def dfs(self, n, tmp):
        if len(tmp) == n:
            self.result.append(self.drawBoard(tmp))
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

    def drawBoard(self, tmp):
        board = []
        for i in xrange(len(tmp)):
            line = ''
            for j in xrange(len(tmp)):
                if j == tmp[i]:
                    line += 'Q'
                else:
                    line += '.'
            board.append(line)
        return board
