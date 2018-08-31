class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = ord('A')
        result = ""
        while n > 0:
            r = (n-1) % 26
            result = chr(base + r) + result
            n = (n-1) / 26
        return result
