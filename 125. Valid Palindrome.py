class Solution(object):
    def isPalindrome(self, s):
        if s is None:
            return False

        l = 0
        h = len(s) - 1

        while l < h:
            while l < h and not s[l].isalpha() and not s[l].isdigit():
                l += 1
            while l < h and not s[h].isalpha() and not s[h].isdigit():
                h -= 1
            if s[l].lower() != s[h].lower():
                return False
            else:
                l += 1
                h -= 1

        return True
