import math
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        if L > R:
            return 0
        result = 0
        for n in xrange(L, R+1):
            count = 0
            while n > 0:
                n &= (n-1)
                count += 1
            if self.checkPrime(count):
                result += 1
        return result

    def checkPrime(self, num):
        if num < 2:   # 1 is not prime number
            return False
        for i in xrange(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
