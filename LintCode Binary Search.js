var binarySearch = function (nums, target) {
    if( nums == null || nums.length == 0 ) {
        return -1;
    }

    var start = 0;
    var end = nums.length - 1;

    a.sort(compare);

    function compare(v1, v2) {
        return v1 - v2;
    }

    while ( start + 1 < end ) {
        var mid = start + Math.floor(( end - start ) / 2);
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            end = mid;
        } else {
            start = mid;
        }
    }
//    console.log(start);
//    console.log(end);

    if( nums[start] == target ) {
        return start;
    }
    if( nums[end] == target ) {
        return end;
    }

    return -1;
};