# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        arr1 = deque()
        arr2 = deque()
        while l1:
            arr1.appendleft(l1.val)
            l1 = l1.next
        while l2:
            arr2.appendleft(l2.val)
            l2 = l2.next
        num1 = int(''.join(str(i) for i in arr1))
        num2 = int(''.join(str(i) for i in arr2))
        num3 = str(num1 + num2)
        dummy = ListNode(-1)
        head = dummy
        for i in xrange(len(num3)-1, -1, -1):
            head.next = ListNode(num3[i])
            head = head.next
        return dummy.next

"""
Solution 2
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        head = dummy
        value = 0
        while l1 or l2 or value:
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            head.next = ListNode(value%10)
            head = head.next
            value /= 10
        return dummy.next
            
        
        