"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        import Queue
        q = Queue.Queue(maxsize=len(graph))
        if values[node] == target:
            return node
        q.put(node)
        del (values[node])

        while q:
            head = q.get()
            for n in head.neighbors:
                if n in values:
                    if values[n] == target:
                        return n
                    del (values[n])
                    q.put(n)
        return None
