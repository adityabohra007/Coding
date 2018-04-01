# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
利用heap进行排序，将每个list的头放入heap中，pop出最小的，然后将它的next再放入heap进行比较

需要注意的是，在python3中，在heap中比较元祖，如果第一个数相同，它会比较第二个数
"""
from heapq import heappop, heappush
class Solution1(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        trav = dummy = ListNode(-1)
        heap = []
        for ll in lists:
            if ll:
                self.heappushNode(heap, ll)
                
        while heap:
            node = heappop(heap)[1]
            trav.next = node
            trav = trav.next
            #print(trav.val)
            if trav.next:
                self.heappushNode(heap, trav.next)
                
                    
        return dummy.next
            
    def heappushNode(self, heap, node):
        heappush(heap, (node.val, node))

"""
两两比较合并
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        l1 = self.mergeKLists(lists[:len(lists)/2])
        l2 = self.mergeKLists(lists[len(lists)/2:])
        
        ret = self.mergeTwoLists(l1, l2)
        
        return ret
    
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        p = ListNode(-1)
        dummyNode = p
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
            
        if l1 is not None:
            p.next = l1
        else:
            p.next = l2
        
        return dummyNode.next
             