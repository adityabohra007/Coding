"""
用二分法找到最左边的点
"""
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        result = [-1, -1]
        if A is None or len(A) == 0:
            return result

        l = 0
        r = len(A)-1
        while l + 1 < r:
            m = (l + r)/2
            if A[m] < target:
                l = m
            else:
                r = m
        if A[l] == target:
            result[0] = l
        elif A[r] == target:
            result[0] = r
        else:
            return result
        i = result[0]
        while i < len(A) and A[i] == target:
            i += 1
        result[1] = i-1
        return result
