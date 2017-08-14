/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {

    var result = [];
    helper ( root );
    return result;

    function helper ( root ) {
        if ( !root ) {
            return;
        }

        result.push ( root.val );
        helper ( root.left );
        helper ( root.right );

    }
};