# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        if root is None:
            return result
        self.dfs(root, str(root.val), result)
        return result

    def dfs(self, root, path, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            result.append(path)
        if root.left:
            self.dfs(root.left, path + '->' + str(root.left.val), result)
        if root.right:
            self.dfs(root.right, path + '->' + str(root.right.val), result)
