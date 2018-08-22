class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        l = 0
        r = len(s)-1
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        while l < r:
            while l < r and s[l].lower() not in vowels:
                l += 1
            while l < r and s[r].lower() not in vowels:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
