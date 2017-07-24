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
 * @return {number}
 */
var pathSum = function(root, sum) {

    var currentSum = 0;
    var array = [];
    var result = [0];

    helper ( root, sum, currentSum, array, result );

    return result[0];

    function helper ( root, sum, currentSum, array, result ) {
        if ( !root ) {
            return;
        }

        currentSum += root.val;
        array.push(root.val);
        var arrayLeft = array.slice();
        var arrayRight = array.slice();

        if ( currentSum == sum ) {
            result[0] ++;
        }

        if ( array.length > 1 ) {
            var tempSum = currentSum;
            for ( var i=0; i < array.length-1; i++ ) {
                tempSum -= array[i];
                if ( tempSum == sum ) {
                    result[0] ++;
                }
            }
        }

        helper( root.left, sum, currentSum, arrayLeft, result );
        helper( root.right, sum, currentSum, arrayRight, result );
    }
};