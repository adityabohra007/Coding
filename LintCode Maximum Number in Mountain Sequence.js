var mountainSequence = function (nums) {
    if ( nums == null || nums.length == 0 ) {
        return -1;
    }

    var mid;
    var start = 0;
    var end = nums.length - 1;

    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );

        if( nums[mid] < nums[mid+1] ) {
            start = mid;
        } else if ( nums[mid] < nums[mid-1] ) {
            end = mid;
        } else {
            return nums[mid];
        }
    }

    if( nums[start] < nums[end] ) {
        return nums[end];
    } else {
        return nums[start];
    }
};