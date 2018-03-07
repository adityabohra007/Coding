/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    if ( nums == null ) {
        return null;
    }

    var max = -Number.MAX_VALUE;
    var sum = 0;
    var minSum = 0;

    for ( var i = 0; i < nums.length; i++ ) {
        sum += nums[i];
        max = Math.max(max, sum - minSum);
        minSum = Math.min(minSum, sum);
    }

    return max;
};