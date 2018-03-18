/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var index;
var result;
var kthSmallest = function(root, k) {
    index = 0;
    inOrder (root, k);
    return result;
};

var inOrder = function (root, k) {
    if (!root) {
        return;
    }

    inOrder(root.left, k);

    index++;

    if (index == k) {
        result = root.val;
    }

    if (index < k) {
        inOrder(root.right, k);
    }
}