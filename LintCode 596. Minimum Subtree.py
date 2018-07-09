"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        if root is None:
            return None
        
        self.m = sys.maxint
        self.result = None
        self.helper(root)
        return self.result
        
    def helper(self, root):
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left + right + root.val < self.m:
            self.m = left + right + root.val
            self.result = root
        
        return left + right + root.val
        
