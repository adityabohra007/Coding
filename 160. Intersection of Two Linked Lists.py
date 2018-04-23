# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        while headA is not None and headB is not None:
            if headA.val == headB.val:
                return headA
            elif headA.val < headB.val:
                headA = headA.next
            else:
                headB = headB.next
