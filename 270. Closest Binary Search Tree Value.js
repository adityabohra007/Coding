/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {number}
 */
var closestValue = function(root, target) {
    if ( root == null ) {
        return 0;
    }

    var result = root.val;
    while (root) {
        if ( Math.abs(root.val - target) < Math.abs(result - target) ) {
            result = root.val
        }
        root = root.val > target ? root.left: root.right;
    }

    return result;
};