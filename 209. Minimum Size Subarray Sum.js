/**
 * @param {number} s
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(s, nums) {

    var result = Number.MAX_VALUE;
    var n = nums.length;
    var sum = 0;

    var left = 0;
    var right = 0;

    while ( right < n ) {
        while ( sum < s ) {
            sum += nums[right++];
        }
        while ( sum >= s ) {
            result = Math.min(result, right - left);
            sum -= nums[left++];
        }
    }

    return result == Number.MAX_VALUE? 0: result;

};