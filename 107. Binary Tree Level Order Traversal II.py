# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def levelOrderBottom(self, root):
        result = deque()
        if root is None:
            return list(result)
        q = deque()
        q.append(root)
        level = 1

        while q:
            l = len(q)
            tmp = []
            for i in xrange(l):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            result.appendleft(tmp)
        return list(result)
