"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        result = []
        if root is None:
            return result

        from collections import deque
        q = deque([root])

        while q:
            qlength = len(q)
            dummy = ListNode(0)
            currNode = dummy
            for i in xrange(qlength):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                currNode.next = ListNode(node.val)
                currNode = currNode.next
            result.append(dummy.next)
        return result
