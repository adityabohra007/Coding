class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        low, high = 1, x / 2 + 1

        while low + 1 < high:
            mid = (low + high) / 2
            if mid * mid < x:
                low = mid
            else:
                high = mid

        if high * high <= x:
            return high
        else:
            return low
