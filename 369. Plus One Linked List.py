# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        h = head
        while h:
            stack.append(h)
            h = h.next
        
        while stack and stack[-1].val == 9:
            stack[-1].val = 0
            stack.pop()
        if stack:
            stack[-1].val += 1
        else:
            node = ListNode(1)
            node.next = head
            head = node
        return head
            
            
        