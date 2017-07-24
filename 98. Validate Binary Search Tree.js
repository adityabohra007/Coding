/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {

    return helper ( root, -(Number.MAX_VALUE), Number.MAX_VALUE );

    function helper ( node, min, max ) {
        if ( !node ){
            return true;
        }

        if ( node.val <= min || node.val >= max ) {
            return false;
        }

        return helper( node.left, min, Math.min(node.val, max) ) && helper( node.right, Math.max(node.val, min), max );
    }
};