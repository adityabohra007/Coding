class Solution(object):
    ALIVE = 1
    DEAD = 0
    BORN = 2
    DYING = -1
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i, j in [(i, j) for i in xrange(len(board)) for j in xrange(len(board[0]))]:
            lives = self.getLives(i, j, board)
            if board[i][j] == self.DEAD and lives == 3:
                board[i][j] = self.BORN
            if board[i][j] == self.ALIVE and lives not in [2, 3]:
                board[i][j] = self.DYING
        for i, j in [(i, j) for i in xrange(len(board)) for j in xrange(len(board[0]))]:
            if board[i][j] == self.BORN:
                board[i][j] = self.ALIVE
            if board[i][j] == self.DYING:
                board[i][j] = self.DEAD
            
    def getLives(self, x, y, board):
        count = 0
        for newX, newY in [(x+i, y+j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not i == j == 0]:
            if newX >= 0 and newX < len(board) and newY >= 0 and newY < len(board[0]) and board[newX][newY] in [self.ALIVE, self.DYING]:
                count += 1
        return count
        
        