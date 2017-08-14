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
var inorderTraversal = function(root) {

    var result = [];
    helper ( root );
    return result;

    function helper ( root ) {
        if (!root) {
            return;
        }

        helper (root.left);
        result.push(root.val);
        helper ( root.right );
    }


};