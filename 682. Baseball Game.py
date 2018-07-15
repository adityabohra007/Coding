class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        q = []
        for op in ops:
            if op == 'C':
                q.pop()
            elif op == 'D':
                q.append(q[-1]*2)
            elif op == '+':
                q.append(q[-1]+q[-2])
            else:
                q.append(int(op))
        return sum(q)
