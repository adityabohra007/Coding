"""
Give a binary tree, and a target number, 
find all path that the sum of nodes equal to target, 
the path could be start and end at any node in the tree.

Example
Given binary tree:

    1
   / \
  2   3
 /
4
and target = 6. Return :
[
  [2, 4],
  [2, 1, 3],
  [3, 1, 2],
  [4, 2]
]
"""
"""
第62 64 66的if判断语句也可以用hash map(visited)来标记被访问过的地方
"""
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum3(self, root, target):
        result = []
        self.dfs(root, target, result)
        return result

    def dfs(self, root, target, result):
        if root is None:
            return
        path = []
        self.findSum(root, None, target, path, result)

        self.dfs(root.left, target, result)
        self.dfs(root.right, target, result)

    def findSum(self, root, father, target, path, result):
        path.append(root.val)
        target -= root.val

        if target == 0:
            result.append(path[:])

        if root.parent not in [None, father]:
            self.findSum(root.parent, root, target, path, result)
        if root.left not in [None, father]:
            self.findSum(root.left, root, target, path, result)
        if root.right not in [None, father]:
            self.findSum(root.right, root, target, path, result)
        path.pop()
