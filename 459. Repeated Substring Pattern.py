class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) < 2:
            return False
        l = len(s)
        for i in xrange(l/2):
            if l % (i+1) == 0:
                if s[:i+1]*(l/(i+1)) == s:
                    return True
        return False
