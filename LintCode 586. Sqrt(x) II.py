class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        lo = 0.0
        hi = x
        diff = 1e-12

        if x < 1.0:
            hi = 1.0

        while hi - lo > diff:
            mid = (hi + lo) / 2
            if mid * mid < x:
                lo = mid
            else:
                hi = mid

        return lo
