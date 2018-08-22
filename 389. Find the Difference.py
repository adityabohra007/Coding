class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for i in xrange(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

# solution 2
class Solution2(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        for c in s+t:
            result ^= ord(c)
        return chr(result)
        