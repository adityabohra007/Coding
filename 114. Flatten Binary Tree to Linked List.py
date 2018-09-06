# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        if root is None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp


"""
Solution 2: no recursion
"""
class Solution2:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if root is None:
            return
        cur = root
        while cur:
            if cur.left:
                node = cur.left
                while node.right:
                    node = node.right
                node.right = cur.right 
                cur.right = cur.left
                cur.left = None
            cur = cur.right
