from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if len(s) < len(p):
            return result
        hash = defaultdict(int)
        for c in p:
            hash[c] += 1
        count = len(p)
        begin, end = 0, 0
        
        while end < len(s):
            if hash[s[end]] > 0:
                count -= 1
            hash[s[end]] -= 1
            end += 1
            
            if count == 0:
                print(end)
                result.append(begin)
            if end - begin == len(p):
                hash[s[begin]] += 1
                if hash[s[begin]] > 0:
                    count += 1
                begin += 1
        return result