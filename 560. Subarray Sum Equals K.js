/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    var n = nums.length;
    var result = 0;
    var map = new Map();
    var sum = 0;

    map.set(0, 1);

    for ( var i = 0; i < n; i++ ) {
        sum += nums[i];
        if ( map.has(sum-k) ) {
            result += map.get(sum-k);
        }
        if ( map.has(sum) ) {
            var value = map.get(sum);
            map.set(sum, value+1);
        } else {
            map.set(sum, 1);
        }
    }

    return result;
};