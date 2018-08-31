# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        heap = []
        dummy = ListNode(-1)
        head = dummy
        if l1:
            heapq.heappush(heap, (l1.val, l1))
        if l2:
            heapq.heappush(heap, (l2.val, l2))
        while len(heap) > 0:
            val, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            head.next = node
            head = head.next
        return dummy.next

"""
Solution 2
"""
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        n1, n2 = 0, 0
        result = []
        
        while n1 < len(A) and n2 < len(B):
            if A[n1] < B[n2]:
                result.append(A[n1])
                n1 += 1
            else:
                result.append(B[n2])
                n2 += 1
        
        if n1 < len(A):
            result += A[n1:]
        if n2 < len(B):
            result += B[n2:]
        return result