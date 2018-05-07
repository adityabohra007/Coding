"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
"""
"""
left - right - root
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.result.append(root.val)
