"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        from collections import defaultdict, deque
        if graph is None:
            return graph

        indegree = defaultdict(int)
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1

        q = deque()
        for node in graph:
            if node not in indegree:
                q.append(node)

        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return result
