# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution_1(object):
    def closestValue(self, root, target):
        min = sys.maxint
        self.result = root.val
        self.dfs(root, target, min)
        return int(self.result)

    def dfs(self, root, target, min):
        if root is None:
            return
        if root.val == target:
            self.result = target
            return
        if abs(root.val - target) < min:
            min = abs(root.val - target)
            self.result = root.val
        if root.val < target:
            self.dfs(root.right, target, min)
        else:
            self.dfs(root.left, target, min)

"""
Solution 2
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution_2(object):
    def closestValue(self, root, target):
        if root is None:
            return None
        result = root.val
        while root:
            if abs(root.val - target) < abs(result - target):
                result = root.val
            root = root.right if root.val < target else root.left
        return result
