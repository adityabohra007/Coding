var lastPosition = function (nums, target) {
    if ( nums == null || nums.length == 0 ) {
        return -1;
    }

    var mid;
    var start = 0;
    var end = nums.length - 1;

    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );

        if ( nums[mid] == target ) {
            start = mid;
        } else if ( nums[mid] < target ) {
            start = mid;
        } else {
            end = mid
        }
    }

    // 先判断 end
    if ( nums[end] == target ) {
        return end;
    }

    if( nums[start] == target ) {
        return start;
    }

    return -1;
};
