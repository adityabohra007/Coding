class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in xrange(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
