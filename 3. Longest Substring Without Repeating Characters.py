class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result = 0
        if len(s) == 0:
            return result
        m = {}
        start = 0
        for i in xrange(len(s)):
            if s[i] in m and m[s[i]] >= start:
                start = m[s[i]] + 1
            m[s[i]] = i
            result = max(result, i - start + 1)
        return result