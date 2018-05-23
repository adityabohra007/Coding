class Solution(object):
    def isUgly(self, num):
        if num < 1:
            return False
        if num == 1:
            return True
        for f in [2, 3, 5]:
            while num % f == 0:
                num = num / f
                if num == 1:
                    return True
        return False