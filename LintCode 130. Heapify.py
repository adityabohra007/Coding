import heapq
class Solution1:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        heapq.heapify(A)

"""
Second solution to heapify array
"""
class Solution2:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):

        for i in range(len(A)):
            self.siftup(A, i)

    def siftup(self, A, i):

        while i != 0:
            father = int((i - 1) / 2)
            if A[father] < A[i]:
                break
            A[father], A[i] = A[i], A[father]
            i = father