/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {boolean}
 */
var hasPathSum = function(root, sum) {

    if ( !root ) {
        return false;
    }
    return helper ( root, 0, sum );

    function helper ( root, subsum, sum ) {

        if ( root ) {
            subsum += root.val;
        } else {
            return false;
        }

        if ( !root.left && !root.right ) {
            return subsum == sum
        }

        var left = helper ( root.left, subsum, sum );
        var right = helper ( root.right, subsum, sum );

        return (left || right);
    }
};