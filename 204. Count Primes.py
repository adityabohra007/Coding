class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        hash = [True] * n
        hash[0] = False
        hash[1] = False
        for i in xrange(2, n):
            if hash[i] == True:
                for j in xrange(2, (n-1)//i+1):
                    hash[i*j] = False
        return sum(hash)
