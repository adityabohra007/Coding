class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}
        for i in xrange(len(s)):
            source = s[i]
            target = t[i]
            if source in hashS and hashS[source] != target:
                return False
            if target in hashT and hashT[target] != source:
                return False
            if source not in hashS:
                hashS[source] = target
            if target not in hashT:
                hashT[target] = source
        return True
