/**
 * @param {number[]} nums
 * @return {number}
 */

/**
 * 不能用nums[0]作为target，因为[1,2,3] [4,5,6,7,1,2,3]
 * 一定要用nums[end]作为target
 */
var findMin = function(nums) {
    if( nums == null || nums.length == 0 ) {
        return -1;
    }

    var start = 0;
    var end = nums.length - 1;
    var target = nums[end];
    var mid;

    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );
        if ( nums[mid] < target ) {
            end = mid;
        } else {
            start = mid;
        }
    }

    if ( nums[start] <= nums[end] ){
        return nums[start];
    } else {
        return nums[end];
    }
};