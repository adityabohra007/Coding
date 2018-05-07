"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
"""
分治法，分成以下四种情况：
1.当前节点有左右子树，分别计算左右子树的minimum depth，返回其中最小值 + 1
2.当前节点只有左子树，返回左子树的minimum depth + 1
3.当前节点只有右子树，返回右子树的minimum depth + 1
4.当前节点没有左右子树（叶子节点），返回1
分析之后，可发现2，3，4可归纳成一条规律。总体的算法如下
1.递归的出口：当前为None，返回0
2.分别计算左右子树的minimum depth, 记为leftDepth 和 rightDepth
3.若当前节点有左右子树，返回min(leftDepth, rightDepth) + 1, 
否则返回max(leftDepth, rightDepth) + 1
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        deepL = self.minDepth(root.left)
        deepR = self.minDepth(root.right)

        if root.left and root.right:
            return min(deepL, deepR) + 1
        else:
            return max(deepL, deepR) + 1
