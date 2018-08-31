class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        if len(s) > len(t):
            s, t = t, s
        change = False
        for i in xrange(len(s)):
            if s[i] != t[i]:
                if len(s) < len(t):
                    return s[i:] == t[i+1:]
                elif len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                return False
        return True
