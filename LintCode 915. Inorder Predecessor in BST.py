"""
Given a binary search tree and a node in it, 
find the in-order predecessor of that node in the BST.

Example
Given root = {2,1,3}, p = 1, return null.
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order successor of the given node in the BST
    """

    def inorderPredecessor(self, root, p):
        self.pre = None
        self.result = None
        self.dfs(root, p)
        return self.result

    def dfs(self, root, p):
        if root is None or self.result is not None:
            return
        self.dfs(root.left, p)
        if root == p:
            self.result = self.pre
        self.pre = root
        self.dfs(root.right, p)
