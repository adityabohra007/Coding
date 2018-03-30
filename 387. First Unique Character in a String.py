class Solution:
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
            