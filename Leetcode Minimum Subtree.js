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
var findSubtree = function(root) {

    var subtreeSum;
    var subtree;

    helper( root );
    return subtree;

    function helper ( root ) {
        if ( !root ) {
            return 0;
        }

        var sum = helper( root.left ) + helper( root.right ) + root.val;
        if ( sum < subtreeSum ) {
            subtreeSum = sum;
            subtree = root.val;
        }

        return sum;
    }
};

