class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        if len(word) == 0:
            return False
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(board, visited, word[1:], i, j):
                        return True
                    else:
                        visited[i][j] = False
        return False

    def dfs(self, board, visited, word, i, j):
        if word == '':
            return True
        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]
        for n in xrange(4):
            x = i + row[n]
            y = j + col[n]
            if x >= 0 and x < len(board) and y >= 0 and y < len(
                    board[0]
            ) and board[x][y] == word[0] and visited[x][y] == False:
                visited[x][y] = True
                if self.dfs(board, visited, word[1:], x, y):
                    return True
                else:
                    visited[x][y] = False
        return False
