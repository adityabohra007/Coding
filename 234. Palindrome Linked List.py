# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 将后半段翻转
        last = slow.next
        # 考虑[1]只有一个node的可能
        if last is None:
            return True
        while last.next:
            tmp = last.next
            last.next = tmp.next
            tmp.next = slow.next
            slow.next = tmp
        # 从头开始比较
        pre = head
        while slow.next:
            slow = slow.next
            if pre.val != slow.val:
                return False
            pre = pre.next
        return True
        