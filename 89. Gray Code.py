# 镜面排列的，n位元的格雷码可以从n-1位元的格雷码以上下镜射后加上新位元的方式快速的得到
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
