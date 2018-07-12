class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        result = self.grayCode(n-1)
        seq = list(result)
        for i in reversed(result):
            seq.append((1 << (n-1)) | i)
        return seq
