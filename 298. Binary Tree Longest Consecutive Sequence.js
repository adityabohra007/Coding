/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestConsecutive = function(root) {
    return helper ( root, null, 0 );

    function helper ( root, parent, lengthWithoutRoot ) {
        if ( !root ) {
            return 0;
        }

        var length = ( parent && (parent.val + 1 == root.val) )? lengthWithoutRoot + 1: 1;
        var left = helper ( root.left, root, length );
        var right = helper ( root.right, root, length );

        return Math.max( length, Math.max( left, right ) );
    }
};