class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        d[n] = 1
        while True:
            sum = 0
            for x in list(str(n)):
                sum += int(x) * int(x)
            if sum == 1 or sum in d:
                break
            else:
                d[sum] = 1
                n = sum
        return sum == 1