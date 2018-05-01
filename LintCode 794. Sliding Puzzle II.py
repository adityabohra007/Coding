class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        st = ""
        ed = ""
        S = set()
        q = []
        fx = [0, 1, 0, -1]
        fy = [1, 0, -1, 0]
        for i in xrange(3):
            for j in xrange(3):
                st += str(init_state[i][j])
                ed += str(final_state[i][j])
        q.append(st)
        S.add(st)
        dp = 0
        while q:
            siz = len(q)
            for i in xrange(siz):
                cur = q.pop(0)
                if cur == ed:
                    return dp
                pos = cur.find('0')
                x, y = pos // 3, pos % 3
                for j in xrange(4):
                    nx, ny = x + fx[j], y + fy[j]
                    if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                        continue
                    tpos = 3 * nx + ny
                    a, b = max(tpos, pos), min(tpos, pos)
                    cur = cur[0:b] + cur[a] + cur[b + 1:
                                                  a] + cur[b] + cur[a + 1:]
                    if (not cur in S):
                        q.append(cur)
                        S.add(cur)
                    cur = cur[0:b] + cur[a] + cur[b + 1:
                                                  a] + cur[b] + cur[a + 1:]
            dp += 1
        return -1