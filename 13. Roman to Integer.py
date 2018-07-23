"""
从后往前遍历
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        result = 0
        cur = 0
        for i in xrange(len(s)-1, -1, -1):
            if hash[s[i]] < cur:
                result -= hash[s[i]]
            else:
                result += hash[s[i]]
            cur = hash[s[i]]
        return result