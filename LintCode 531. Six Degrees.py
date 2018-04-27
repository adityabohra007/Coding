"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        q = []
        ref = {}

        q.append(s)
        ref[s] = 0

        while q:
            node = q.pop(0)
            if node == t:
                return ref[node]
            for neighbor in node.neighbors:
                if neighbor not in ref:
                    q.append(neighbor)
                    ref[neighbor] = ref[node] + 1
        return -1
