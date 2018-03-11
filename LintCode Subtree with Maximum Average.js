/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode} max
 */
var findSubtree2 = function( root ) {

    function ResultType( sum, size) {
        this.sum = sum;
        this.size = size;
    }

    var subtree = new TreeNode;
    var subtreeResult = new ResultType;
    helper ( root );
    return subtree;

    function helper( root ) {
        if ( !root ) {
            return new ResultType(0, 0);
        }

        var left = helper( root.left );
        var right = helper( root.right );
        var result = new ResultType(
            left.sum + right.sum + root.val,
            left.size + right.size + 1
        );

        if ( subtree == null || subtreeResult.sum * result.size < result.sum * subtreeResult.size ) {
            subtree = root;
            subtreeResult = result;
        }

        return result;
    }

};