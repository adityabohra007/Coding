class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N is None or N < 1:
            return 0
        result = [0]
        visited = [False] * N
        self.helper(N, visited, result, 0)
        return result[0]

    def helper(self, n, visited, result, index):
        if index == n:
            result[0] += 1
            return
        for i in xrange(1, n+1):
            if visited[i-1] or i % (index+1) != 0 and (index+1) % i != 0:
                continue
            visited[i-1] = True
            self.helper(n, visited, result, index+1)
            visited[i-1] = False
