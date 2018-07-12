class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash = {}
        for c in s:
            if c not in hash:
                hash[c] = 1
            else:
                hash[c] += 1

        for c in t:
            if c not in hash:
                return False
            if hash[c] == 0:
                return False
            hash[c] -= 1

        for v in hash.values():
            if v > 0:
                return False
        return True
