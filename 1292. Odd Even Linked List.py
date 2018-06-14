"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        if head is None:
            return head

        odd = head
        even = head.next
        while even and even.next:
            taken = even.next

            even.next = taken.next
            taken.next = odd.next
            odd.next = taken

            odd = odd.next
            even = even.next

        return head