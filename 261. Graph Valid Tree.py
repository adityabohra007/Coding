class Solution(object):
    def validTree(self, n, edges):
        if n != len(edges) + 1:
            return False

        map = collections.defaultdict(list)
        for i, j in edges:
            map[i].append(j)
            map[j].append(i)

        import Queue
        q = Queue.Queue()
        visited = {}

        q.put(0)

        while not q.empty():
            cur = q.get()
            visited[cur] = True
            for node in map[cur]:
                if node not in visited:
                    q.put(node)

        return len(visited) == n
