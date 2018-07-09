from collections import defaultdict
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        hash = defaultdict(int)
        for c in S:
            hash[c] += 1
        result = 0
        for c in J:
            result += hash[c]
        return result
            