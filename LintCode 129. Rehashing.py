"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        size = 2 * len(hashTable)
        result = [None for _ in xrange(size)]
        for node in hashTable:
            cur = node
            while cur != None:
                self.addNode(result, cur.val)
                cur = cur.next
        return result
    
    def addNode(self, result, val):
        pos = val % len(result)
        if result[pos] == None:
            result[pos] = ListNode(val)
        else:
            self.addListNode(result[pos], val)
    
    def addListNode(self, node, val):
        while node.next:
            node = node.next
        node.next = ListNode(val)
        