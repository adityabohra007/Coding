# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        self.result = []
        self.helper(root)
        self.result = list(set(self.result))
        if len(self.result) < 2:
            return -1
        self.result = sorted(self.result)
        return self.result[1]
    
    def helper(self, root):
        if root is None:
            return
        self.result.append(root.val)
        self.helper(root.left)
        self.helper(root.right)
                    
                
        