class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        cur = [1]
        result = []
        for i in xrange(1, numRows+1):
            result.append(cur)
            pre = cur
            cur = [1]
            for j in xrange(i-1):
                cur.append(pre[j]+pre[j+1])
            cur.append(1)
        return result
