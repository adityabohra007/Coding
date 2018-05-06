"""
Given a binary tree, find the subtree with maximum average. 
Return the root of the subtree.

Example

Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
return the node 11.
"""
"""
特别注意 sum * 1.0 / ave 这样才会出现小数点，不乘以1.0，是直接整数
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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        self.ave = -sys.maxint
        self.node = root
        self.dfs(root)
        return self.node

    def dfs(self, root):
        if root is None:
            return 0, 0
        sumL, sizeL = self.dfs(root.left)
        sumR, sizeR = self.dfs(root.right)

        sum, size = sumL + sumR + root.val, sizeL + sizeR + 1

        if sum * 1.0 / size > self.ave:
            self.ave = sum * 1.0 / size
            self.node = root

        return sum, size
