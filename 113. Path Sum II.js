/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    var result = [];
    if ( !root ) {
        return result;
    }

    helper ( root, result, root.val, [root.val] );

    return result;

    function helper ( root, result, subsum, subArray ) {
        if ( !root ) {
            return;
        }

        if ( !root.left && !root.right ) {
            if ( subsum == sum ) {
                result.push(subArray);
                return;
            }
        }

        if ( root.left ) {
            var subArrayLeft = subArray.slice();
            subArrayLeft.push(root.left.val);
            helper ( root.left, result, (subsum+root.left.val), subArrayLeft );
        }

        if ( root.right ) {
            var subArrayRight = subArray.slice();
            subArrayRight.push(root.right.val);
            helper ( root.right, result, (subsum+root.right.val), subArrayRight );
        }
    }
};

// another approach
var pathSumII = function(root, sum) {

    var result = [];
    helper ( root, sum, 0, [] );
    return result;

    function helper ( root, sum, subsum, subArray ) {
        if ( root ) {
            subsum += root.val;
            subArray.push(root.val)
            var arrayCopy1 = subArray.slice();
            var arrayCopy2 = subArray.slice();
        } else {
            return false;
        }

        if ( !root.left && !root.right ) {
            if ( subsum == sum ) {
                result.push( subArray );
            }
        }

        helper ( root.left, sum, subsum, arrayCopy1 );
        helper ( root.right, sum, subsum, arrayCopy2 );

    }
};