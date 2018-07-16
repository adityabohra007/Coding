# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.result = ""
        if t is None:
            return self.result
        self.helper(t)
        return self.result

    def helper(self, root):
        if root is None:
            return
        self.result += str(root.val)
        if root.left:
            self.result += '('
            self.helper(root.left)
            self.result += ')'
        elif root.right:
            self.result += '()'
        if root.right:
            self.result += '('
            self.helper(root.right)
            self.result += ')'
