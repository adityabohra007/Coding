var closestNumber = function (nums, target) {
    if( nums == null || nums.length == 0 ) {
        return -1;
    }

    var start = 0;
    var end = nums.length - 1;

    while ( start + 1 < end ) {
        var mid = start + Math.round((end - start) / 2);
        if( nums[mid] == target ) {
            return mid;
        } else if ( nums[mid] > target ) {
            end = mid;
        } else {
            start = mid
        }
    }

    if( Math.abs( nums[start] - target ) <= Math.abs( nums[end] - target ) ) {
        return start;
    } else {
        return end;
    }
};