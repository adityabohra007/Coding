# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        hash = {}
        q = [root]
        while q:
            node = q.pop()
            if k - node.val in hash:
                return True
            hash[node.val] = 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
        
        