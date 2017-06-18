/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    if( nums == null || nums.length == 0 ) {
        return -1;
    }

    var start = 0;
    var end = nums.length - 1;
    var mid;

    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );
        if ( nums[mid] < nums[end] ){
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