# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, lo, hi):
        if lo > hi:
            return
        cur = lo
        for i in xrange(lo, hi+1):
            if nums[i] > nums[cur]:
                cur = i
        root = TreeNode(nums[cur])
        root.left = self.helper(nums, lo, cur-1)
        root.right = self.helper(nums, cur+1, hi)
        return root
        