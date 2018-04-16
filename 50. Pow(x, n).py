class Solution(object):
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
