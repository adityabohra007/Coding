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
var maxDepth = function(root) {
    if ( !root ) {
        return 0;
    }

    var left = maxDepth( root.left );
    var right = maxDepth( root.right );

    return Math.max( left, right ) + 1;
};

// 另一种写法
var maxDepthII = function(root) {
    return helper ( root, 0 );

    function helper( root, depth ) {
        if ( !root ){
            return depth;
        }

        depth += 1;

        var leftPart = helper( root.left, depth );
        var rightPart = helper( root.right, depth );

        return Math.max( leftPart, rightPart );
    }
};