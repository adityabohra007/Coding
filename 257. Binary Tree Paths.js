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

    if ( !root ) {
        return result;
    }

    helper( root, result, root.val.toString() );

    return result;

    function helper ( root, result, path ) {
        if ( !root ) {
            return;
        }

        if ( !root.left && !root.right ) {
            result.push( path );
            return;
        }

        if ( root.left ) {
            helper( root.left, result, (path + '->' + root.left.val).toString() );
        }

        if ( root.right ) {
            helper( root.right, result, (path + '->' + root.right.val).toString() );
        }
    }


};