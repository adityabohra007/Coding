class Solution_1(object):
    def divide(self, dividend, divisor):
        if dividend is None or divisor is None:
            return False

        low = 0
        high = abs(dividend)
        INT_MAX = 2147483647

        while low + 1 < high:
            mid = (low + high) / 2
            if mid * abs(divisor) < abs(dividend):
                low = mid
            else:
                high = mid

        if high * abs(divisor) <= abs(dividend):
            ret = high
        else:
            ret = low

        if dividend * divisor < 0:
            ret *= -1

        if ret > INT_MAX:
            ret -= 1

        return ret

"""
通过位运算
结果一定是一个能表示为二进制的数，所以先从31开始，往下减
"""
class Solution_2(object):
    def divide(self, dividend, divisor):
        INT_MAX = (1 << 31) - 1

        if divisor == 0:
            return INT_MAX
        neg = True if dividend * divisor < 0 else False
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        shift = 31

        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1

        if neg:
            ans = -ans
        if ans > INT_MAX:
            ans = INT_MAX
        return ans
