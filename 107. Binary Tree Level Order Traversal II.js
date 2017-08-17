/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
    if ( !root ) {
        return [];
    }

    var result = [];
    var queue = [];
    queue.push( root );

    while ( queue.length > 0 ) {
        var length = queue.length;
        var level = [];

        for ( var i = 0; i < length; i++ ) {
            var node = queue.shift();
            level.push( node.val );
            if ( node.left ) {
                queue.push ( node.left );
            }
            if ( node.right ) {
                queue.push ( node.right );
            }
        }

        result.unshift( level );
    }

    return result;
};