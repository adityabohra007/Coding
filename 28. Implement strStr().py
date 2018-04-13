class Solution(object):
    def strStr(self, haystack, needle):
        if haystack is None or needle is None:
            return -1
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        for i in xrange(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if haystack[i + j] == needle[j]:
                    j += 1
                else:
                    j = 0
                    break
            if j == len(needle):
                return i

        return -1
