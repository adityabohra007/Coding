class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num//2
        while left + 1 < right:
            mid = (left + right) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid
            else:
                right = mid
        if left * left == num:
            return True
        if right * right == num:
            return True
        return False
