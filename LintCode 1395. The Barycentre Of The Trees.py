class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    ansNode = 0
    ansSize = 0
    def dfs(self, x, f, n, dp, g):
        dp[x] = 1
        maxSubtree = 0
        for i in g[x]:
            if(i == f):
                continue
            self.dfs(i, x, n, dp, g)
            dp[x] += dp[i]
            maxSubtree = max(maxSubtree, dp[i])
        maxSubtree = max(maxSubtree, n - dp[x])
        if((maxSubtree < self.ansSize) or (maxSubtree == self.ansSize and x < self.ansNode)):
            self.ansNode, self.ansSize = x, maxSubtree
    def getBarycentre(self, x, y):
        # Write your code here
        n = len(x) + 1
        g = [ [] for i in range(n + 1) ]
        dp = [ 0 for i in range(n + 1) ]
        for i in range(len(x)):
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])
        self.ansNode = 0
        self.ansSize = n +1
        self.dfs(4, 0, n, dp, g)
        print(dp)
        return self.ansNode