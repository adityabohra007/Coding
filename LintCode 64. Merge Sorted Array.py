class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):

        m = m - 1
        n = n - 1
        l = m + n + 1

        while m >= 0 and n >= 0:
            if A[m] > B[n]:
                A[l] = A[m]
                m, l = m - 1, l - 1
            else:
                A[l] = B[n]
                n, l = n - 1, l - 1

        while n >= 0:
            A[l] = B[n]
            n, l = n - 1, l - 1
