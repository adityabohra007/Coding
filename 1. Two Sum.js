/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if ( nums == null || nums.length == 0 ) {
        return null;
    }
    var n = nums.length;

    var map = new Map();
    for ( var i = 0; i < n; i++ ) {
        map.set(nums[i], i);
    }

    for ( var j = 0; j < n; j++ ) {
        var searched = target - nums[j];
        if ( map.has(searched) && map.get(searched) != j ) {
            var index = map.get(searched);
            if ( index < j ) {
                return [index, j];
            } else {
                return [j, index];
            }
        }
    }
};