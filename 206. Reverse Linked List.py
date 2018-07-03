# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = None
        while head:
            tmp = head.next
            head.next = curr
            curr = head
            head = tmp
        return curr
        