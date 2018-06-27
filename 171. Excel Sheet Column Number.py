class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s) - 1, -1, -1):
            result += (ord(s[i]) - 64) * pow(26, len(s) - 1 - i)
        return result