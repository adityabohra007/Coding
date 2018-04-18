class Solution:
    """
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """

    def closestNumber(self, A, target):
        if not A or len(A) == 0 or target is None:
            return -1

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = (low + high) / 2
            if A[mid] < target:
                low = mid
            else:
                high = mid

        return low if (abs(A[low] - target) < abs(A[high] - target)) else high
