# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        tail = ListNode(-1)
        while head:
            tmp = tail.next
            tail.next = head
            head = head.next
            tail.next.next = tmp
        return tail.next
