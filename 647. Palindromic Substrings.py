class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        length = len(s)
        for i in xrange(2*length-1):
            left = right = i//2
            if i & 1:
                right += 1

            while left >= 0 and right < length and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        return result
