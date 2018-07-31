class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def findSubstring(self, str, k):
        # Write your code here
        if len(str) < k:
            return 0
        hash = {}
        result = 0
        for i in xrange(len(str)-k+1):
            c = str[i:i+k]
            if c in hash or not self.check(c):
                continue
            result += 1
            hash[c] = 1
        return result
    
    def check(self, s):
        char = {}
        for c in s:
            if c in char:
                return False
            char[c] = 1
        return True