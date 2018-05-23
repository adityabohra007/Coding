"""
Version 1
"""
class Solution_1:
    def firstUniqChar(self, s):
        alp = {}
        for char in s:
            if char not in alp:
                alp[char] = 1
            else:
                alp[char]+= 1
        
        index = 0
        for char in s:
            if alp[char] == 1:
                return index
            index += 1
        
        return -1
            
"""
Version 2
"""
class Solution_2(object):
    def firstUniqChar(self, s):
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        
        for i in xrange(len(s)):
            if map[s[i]] == 1:
                return i
        return -1