"""
Given a binary search tree and a node in it, 
find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        self.pre = None
        self.result = None
        self.dfs(root, p)
        return self.result

    def dfs(self, root, p):
        if root is None or self.result is not None:
            return
        self.dfs(root.left, p)
        if self.pre == p:
            self.result = root
        self.pre = root
        self.dfs(root.right, p)
