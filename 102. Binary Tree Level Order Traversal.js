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
var levelOrder = function(root) {
    var result = [];
    if ( !root ) {
        return result;
    }

    var q = [];
    q.push(root);

    while ( q.length > 0 ) {
        var level = [];
        var length = q.length
        for ( var i = 0; i < length; i++ ) {
            var node = q.shift();
            level.push( node.val );
            if ( node.left ){
                q.push( node.left );
            }
            if ( node.right ){
                q.push( node.right );
            }
        }
        result.push( level );
    }

    return result;
};