from collections import Counter
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """

    def minWindow(self, source, target):
        s = source
        t = target
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

"""
Solution 2
"""
from collections import defaultdict
class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        missing = len(t)
        
        i = I = J = 0
        for j in xrange(len(s)):
            c = s[j]
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if J == 0 or j + 1 - i <= J - I:
                    I, J = i, j+1
        return s[I:J]
                
        