/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {

    var result = [];
    if ( root ) {
        helper ( root, root.val.toString() );
    }
    return result;

    function helper ( root, path ) {
        if ( !root ) {
            return;
        }

        if ( !root.left && !root.right ) {
            result.push ( path );
        }

        if ( root.left ){
            helper ( root.left, (path+'->'+root.left.val).toString() );
        }

        if ( root.right ) {
            helper ( root.right, (path+'->'+root.right.val).toString() );
        }
    }
};