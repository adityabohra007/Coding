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



"""
方法2：
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1, l2 = 0, 0
        node1, node2 = headA, headB
        while node1:
            l1 += 1
            node1 = node1.next
        while node2:
            l2 += 1
            node2 = node2.next

        node1, node2 = headA, headB
        while l1 > l2:
            node1 = node1.next
            l1 -= 1
        while l2 > l1:
            node2 = node2.next
            l2 -= 1
        while node1 and node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1

