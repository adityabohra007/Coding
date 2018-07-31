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
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        if root is None:
            return None
        self.result = None
        self.max = -sys.maxint
        self.helper(root)
        return self.result
        
    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l + r + root.val > self.max:
            self.max = l + r + root.val
            self.result = root
        return l + r + root.val