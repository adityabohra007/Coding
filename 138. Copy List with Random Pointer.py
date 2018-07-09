# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        hash = {}
        chead = RandomListNode(head.label)
        hash[head] = chead
        p = head
        q = chead
        # 建立next的映射
        while p:
            q.random = p.random
            if p.next:
                q.next = RandomListNode(p.next.label)
                hash[p.next] = q.next
            else:
                q.next = None
            p = p.next
            q = q.next
        
        # 建立random的映射
        p = chead
        while p:
            if p.random:
                p.random = hash[p.random]
            p = p.next
        return chead
                