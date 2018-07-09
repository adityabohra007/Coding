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

"""
Solution 2
"""
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        result = 0
        hash = {}
        tmp = ''
        for i in xrange(len(s)):
            c = s[i]
            if c in tmp:
                tmp = s[hash[c]+1:i+1]
            else:
                tmp += c
            hash[c] = i
            if len(tmp) > result:
                result = len(tmp)
        return result