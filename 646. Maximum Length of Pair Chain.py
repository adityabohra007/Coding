import sys
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        result = 0
        if pairs is None or len(pairs) == 0:
            return result
        pairs = sorted(pairs, key=lambda x: x[1])
        cur = -sys.maxint
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                result += 1
        return result