class Solution_1(object):
    def myPow(self, x, n):
        if n < 0:
            v = 1 / self.helper(x, -n)
        else:
            v = self.helper(x, n)

        return v

    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        value = self.helper(x, n / 2)

        if n & 1:
            return value * value * x
        else:
            return value * value

"""
Solution 2
"""
class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        ret = 1
        tmp = x

        while n != 0:
            if n & 1:
                ret *= tmp
            tmp *= tmp
            n = n >> 1

        return ret
