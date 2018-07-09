# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 
        self.result = -sys.maxint
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if root is None:
            return 0
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        total = root.val + left + right
        if total > self.result:
            self.result = total
        return max(left, right) + root.val