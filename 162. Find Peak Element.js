/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    if ( nums == null || nums.length == 0 ) {
        return -1;
    }

    var mid;
    var start = 0;
    var end = nums.length - 1;

    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );

        if( nums[mid-1] > nums[mid] ) {
            end = mid;
        } else if ( nums[mid] < nums[mid+1] ) {
            start = mid;
        } else {
            start = mid;
        }
    }

    if( nums[start] < nums[end] ) {
        return end;
    } else {
        return start;
    }
};