# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        q = []
        q.append(root)
        while len(q) > 0:
            length = len(q)
            row = []
            for i in xrange(length):
                node = q.pop(0)
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(row)
        return result
