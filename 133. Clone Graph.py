# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

"""
将graph上的每个node都放到map上
"""
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return node

        root = node
        import Queue
        q = collections.deque([node])
        nodes = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in nodes:
                    nodes.add(neighbor)
                    q.append(neighbor)

        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        for node in nodes:
            newNode = mapping[node]
            for neighbor in node.neighbors:
                newNeighbor = mapping[neighbor]
                newNode.neighbors.append(newNeighbor)

        return mapping[root]
