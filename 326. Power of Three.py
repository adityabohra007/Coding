class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 2:
            if (n % 3) != 0:
                return False
            n = n // 3
        if n == 2:
            return False
        return True
