class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        from collections import defaultdict
        edges = defaultdict(list)
        indgrees = defaultdict(int)
        nodes = set()

        for seq in seqs:
            nodes |= set(seq)
            for i in xrange(len(seq)):
                if i == 0:
                    indgrees[seq[i]] += 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indgrees[seq[i + 1]] += 1
        q = [k for k in indgrees if indgrees[k] == 0]
        result = []

        while len(q) == 1:
            cur_node = q.pop()
            result.append(cur_node)
            for node in edges[cur_node]:
                indgrees[node] -= 1
                if indgrees[node] == 0:
                    q.append(node)
        if len(q) > 1:
            return False
        return result == org and len(result) == len(nodes)
