class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        p1 = len(A)
        p2 = len(B)
        i, j = 0, 0
        c = []
        while (i < p1) and (j < p2):
            if A[i] < B[j]:
                c.append(A[i])
                i += 1
            else:
                c.append(B[j])
                j += 1
        while i < p1:
            c.append(A[i])
            i += 1
        while j < p2:
            c.append(B[j])
            j += 1
        return c
