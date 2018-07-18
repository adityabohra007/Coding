from collections import deque
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        w, h = len(board), len(board[0])

        def countBoard(i, j):
            cnt = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= w or nj < 0 or nj >= h:
                        continue
                    if board[ni][nj] == 'M':
                        cnt += 1
            return str(cnt) if cnt else 'B'
        cx, cy = click
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
            return board
        q = [click]
        board[cx][cy] = countBoard(cx, cy)
        if board[cx][cy] != 'B':
            return board
        while q:
            ti, tj = q.pop(0)
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = ti + di, tj + dj
                    if ni < 0 or ni >= w or nj < 0 or nj >= h:
                        continue
                    if board[ni][nj] == 'E':
                        board[ni][nj] = countBoard(ni, nj)
                        if board[ni][nj] == 'B':
                            q.append((ni, nj))
        return board
