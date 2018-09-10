# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return
        dummyNode = ListNode(-1)
        dummyNode.next = head
        head = dummyNode
        while True:
            head = self.helper(head, k)
            if head is None:
                break
        return dummyNode.next

    # head -> n1 -> n2 -> n3 -> n4 -> n5 -> n6 -> ..... -> nk -> nk+1
    def helper(self, head, k):
        nk = head
        for i in xrange(k):
            if nk is None:
                return None
            nk = nk.next
        if nk is None:
            return None
        n1 = head.next

        while head.next != nk:
            tmp = n1.next.next
            n1.next.next = head.next
            head.next = n1.next
            n1.next = tmp
        return n1
