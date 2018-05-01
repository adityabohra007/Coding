"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque


class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """

    def connectedSet(self, nodes):
        visited = {}
        result = []
        import Queue
        for node in nodes:
            if node not in visited:
                q = deque()
                q.append(node)
                visited[node] = True
                tmp = []
                while q:
                    cur = q.popleft()
                    tmp.append(cur.label)
                    for neighbor in cur.neighbors:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited[neighbor] = True
                result.append(sorted(tmp))
        return result
