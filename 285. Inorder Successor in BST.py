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


class Solution_1(object):
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

"""
二分循环搜索可能的candidate
"""


class Solution_2:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        result = None
        while root is not None:
            if root.val <= p.val:
                root = root.right
            else:
                result = root
                root = root.left
        return result
