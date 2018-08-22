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


class Solution2(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        row = self.getRow(rowIndex - 1)
        tmp = [0] + row + [0]
        result = []
        for i in xrange(len(tmp)-1):
            result.append(tmp[i]+tmp[i+1])
        return result
