# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        self.hash = {}
        self.m = 0
        self.helper(root)
        for k, v in self.hash.items():
            if v == self.m:
                result.append(k)
        return result
    
    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        total = l + r + root.val
        if total in self.hash:
            self.hash[total] += 1
        else:
            self.hash[total] = 1
        if self.hash[total] > self.m:
            self.m = self.hash[total]
        return total
        