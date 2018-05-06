# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
is 5 but its right child's value is 4.
"""
"""
中序排列
前面一个一定小于后面
这个成立的前提是 left<root<right，如果出现<= 或者 >=就不能用这个方法
"""
class Solution(object):
    def isValidBST(self, root):
        self.cur = None
        self.isBST = True
        self.dfs(root)
        return self.isBST

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        if self.cur is not None and self.cur >= root.val:
            self.isBST = False
        self.cur = root.val
        self.dfs(root.right)

"""
方法2: left的最大值一定是一路下来最小的，right的最小值一定是一路下来最大的
"""
import sys


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        return self.dfs(root, -sys.maxint, sys.maxint)

    def dfs(self, root, minValue, maxValue):
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        return self.dfs(root.left, minValue,
                        min(root.val, maxValue)) and self.dfs(
                            root.right, max(root.val, minValue), maxValue)
