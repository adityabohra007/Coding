class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        if str is None or len(str) == 0:
            return
        start, end = 0, len(str)-1
        while start < end:
            str[start], str[end] = str[end], str[start]
            start, end = start+1, end-1

        start = 0
        while start < len(str):
            end = start + 1
            while end < len(str) and str[end] != ' ':
                end += 1
            wordEnd = end - 1
            while start < wordEnd:
                str[start], str[wordEnd] = str[wordEnd], str[start]
                start, wordEnd = start+1, wordEnd-1
            start = end + 1
