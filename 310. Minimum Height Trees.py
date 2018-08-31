class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n != len(edges)+1 or n == 0:
            return []
        a = [0] * n
        b = {}
        result = [0]
        for edge in edges:
            a[edge[0]] += 1
            a[edge[1]] += 1
            if edge[0] in b:
                b[edge[0]].append(edge[1])
            else:
                b[edge[0]] = [edge[1]]
            if edge[1] in b:
                b[edge[1]].append(edge[0])
            else:
                b[edge[1]] = [edge[0]]

        q = []
        for i in xrange(len(a)):
            if a[i] == 1:
                q.append(i)

        while q:
            result = []
            newq = []
            for n in q:
                result.append(n)
                for child in b[n]:
                    a[child] -= 1
                    if a[child] == 1:
                        newq.append(child)
            q = newq
        return result
