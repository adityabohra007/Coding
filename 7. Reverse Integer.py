class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x is None:
            return
        x = str(x)
        q = 1
        if x[0] == '-':
            x = x[1:]
            q = -1
        x = list(x)
        l, r = 0, len(x)-1
        while l < r:
            x[l], x[r] = x[r], x[l]
            l += 1
            r -= 1
        result = int("".join(x)) * q
        if result < -(1 << 31) or result > (1 << 31) - 1:
            return 0
        return result
