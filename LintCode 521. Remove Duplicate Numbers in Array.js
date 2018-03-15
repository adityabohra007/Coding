var deduplication = function (nums) {
    var map = new Map();
    var n = nums.length;
    for ( var i = 0; i < n; i++ ) {
        if ( map.has(nums[i]) ) {
            continue;
        }
        map.set(nums[i], true);
    }

    var result = 0;
    for ( var k of map.keys() ) {
        nums[result++] = k;
    }

    return result;

};