class Solution_1:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        if not A or len(A) == 0 or target is None:
            return 0

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = (low + high) / 2
            if A[mid] < target:
                low = mid
            else:
                high = mid

        if A[low] == target:
            index = low
        elif A[high] == target:
            index = high
        else:
            return 0

        total = 1
        for i in xrange(index + 1, len(A)):
            if A[i] == target:
                total += 1
            else:
                return total

        return total



"""
用2次二分法
"""
class Solution_2:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        if not A or len(A) == 0 or target is None:
            return 0

        low = 0
        high = len(A) - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if A[mid] < target:
                low = mid
            else:
                high = mid

        if A[low] == target:
            head = low
        elif A[high] == target:
            head = high
        else:
            return 0

        low = 0
        high = len(A) - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if A[mid] <= target:
                low = mid
            else:
                high = mid

        if A[high] == target:
            tail = high
        elif A[low] == target:
            tail = low

        return tail - head + 1
