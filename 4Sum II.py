class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash = {}
        for a in A:
            for b in B:
                if a + b in hash:
                    hash[a + b] += 1
                else:
                    hash[a + b] = 1
        result = 0
        for c in C:
            for d in D:
                if -c - d in hash:
                    result += hash[-c - d]
        return result