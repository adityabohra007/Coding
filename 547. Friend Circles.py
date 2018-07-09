class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0:
            return -1
        if len(M[0]) == 0:
            return -1
        q = []
        result = 0
        used = [0 for _ in xrange(len(M))]
        for i in xrange(len(M)):
            if M[i][i] == 1:
                result += 1
                q.append(i)
                while q:
                    point = q.pop(0)
                    used[point] = 1
                    M[point][point] = 0
                    for j in xrange(len(M)):
                        if M[j][point] == 1 and used[j] == 0:
                            q.append(j)
        return result