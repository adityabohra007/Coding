# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        dummyNode = ListNode(-1)
        dummyNode.next = head
        tail = dummyNode
        while tail.next and tail.next.next:
            tmp1 = tail.next.next.next
            tmp2 = tail.next
            tail.next = tail.next.next
            tail.next.next = tmp2
            tmp2.next = tmp1
            tail = tail.next.next
        return dummyNode.next
            
            
            