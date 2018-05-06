"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

Example

For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
要考虑A B两个node有不存在情况
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.dfs(root, A, B)
        if a and b:
            return lca
        else:
            return None

    def dfs(self, root, A, B):
        if root is None:
            return False, False, None

        aLeft, bLeft, nodeLeft = self.dfs(root.left, A, B)
        aRight, bRight, nodeRight = self.dfs(root.right, A, B)

        a = aLeft or aRight or root == A
        b = bLeft or bRight or root == B

        if root == A or root == B:
            return a, b, root

        if nodeLeft is not None and nodeRight is not None:
            return a, b, root
        if nodeLeft is not None:
            return a, b, nodeLeft
        if nodeRight is not None:
            return a, b, nodeRight

        return a, b, None