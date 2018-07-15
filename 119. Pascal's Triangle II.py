class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        cur = [1]
        if rowIndex == 1:
            return cur
        for i in xrange(rowIndex):
            pre = cur
            cur = [1]
            for j in xrange(i-1):
                cur.append(pre[j]+pre[j+1])
            cur.append(1)
        return cur
