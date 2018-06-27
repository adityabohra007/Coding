class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        i = 1
        while pow(5, i) <= n:
            result += n // pow(5, i)
            i += 1
        return result