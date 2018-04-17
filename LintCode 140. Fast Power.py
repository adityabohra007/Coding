class Solution_1:
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

"""
Solution 2
"""


class Solution_2:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):

        if n == 0:
            return 1 % b
        elif n == 1:
            return a % b
        else:
            value = self.fastPower(a, b, n / 2)

            if n & 1:
                return (value * value * a) % b
            else:
                return (value * value) % b
