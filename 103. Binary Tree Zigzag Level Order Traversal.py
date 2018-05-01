# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def zigzagLevelOrder(self, root):
        result = []
        if root is None:
            return result
        q = deque()
        q.append(root)
        level = 1

        while q:
            l = len(q)
            tmp = deque()
            for i in xrange(l):
                node = q.popleft()
                if level % 2 == 1:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            result.append(list(tmp))
        return result
