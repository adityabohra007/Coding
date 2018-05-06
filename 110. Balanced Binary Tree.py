# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        return self.dfs(root) != -1

    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
