class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 1:
            return 0
        hash = {}
        head = 0
        result = 0
        for i in xrange(len(s)):
            if s[i] in hash:
                hash[s[i]] += 1
            else:
                hash[s[i]] = 1
                while len(hash) > 2:
                    c = s[head]
                    hash[c] -= 1
                    head += 1
                    if hash[c] == 0:
                        del (hash[c])
            result = max(result, i - head + 1)
        return result
