class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):

        ret = 1

        while n != 0:
            if n & 1:
                ret = ret * a % b
            a = a * a % b
            n = n >> 1

        return ret % b
