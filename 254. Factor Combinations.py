class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        if n is None or n == 0:
            return self.result
        self.helper(n, [], 2)
        return self.result
    
    def helper(self, n, tmp, index):
        if n == 1:
            if len(tmp) > 1:
                self.result.append(tmp)
            return
        for i in xrange(index, n+1):
            if n % i == 0:
                self.helper(n/i, tmp+[i], i)
        
"""
Solution 2
特别的: **是幂运算
"""       
class Solution2(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        if n is None or n == 0:
            return self.result
        self.helper(n, [], 2)
        return self.result
    
    def helper(self, n, tmp, index):
        for i in xrange(index, int(n**0.5)+1):
            div, rem = divmod(n, i)
            if rem == 0 and div >= i:
                tmp.append(i)
                self.result.append(tmp[:]+[div])
                self.helper(div, tmp, i)
                tmp.pop()
        