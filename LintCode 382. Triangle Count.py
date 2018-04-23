class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        result = 0
        S = sorted(S, reverse=True)

        for i in xrange(len(S) - 2):
            lo = i + 1
            hi = len(S) - 1
            while lo < hi:
                total = S[lo] + S[hi]
                if total > S[i]:
                    result += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return result
