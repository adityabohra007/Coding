"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None
        dummy = head = ListNode(-1)
        heap = []
        for list in lists:
            if list:
                heapq.heappush(heap, (list.val, list))
        while heap:
            node = heapq.heappop(heap)
            if node[1].next:
                heapq.heappush(heap, (node[1].next.val, node[1].next))
            head.next = node[1]
            head = head.next
        return dummy.next