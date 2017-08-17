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
var zigzagLevelOrder = function(root) {
    if ( !root ) {
        return [];
    }

    var result = [];
    var queue = [];
    queue.push( root );
    var index = 1;

    while ( queue.length > 0 ) {
        var length = queue.length;
        var level = [];

        for ( var i = 0; i < length; i++ ) {
            var node = queue.shift();
            if ( (index + 1) % 2 == 0 ) {
                level.push( node.val );
            } else {
                level.unshift( node.val );
            }

            if ( node.left ) {
                queue.push( node.left );
            }

            if ( node.right ) {
                queue.push( node.right );
            }
        }

        result.push( level );
        index ++;
    }

    return result;
};