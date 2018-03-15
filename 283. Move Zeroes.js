/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {

    var n = nums.length;
    var n0 = 0;

    for ( var i = 0; i < n; i++ ) {
        if ( nums[i] == 0 ) {
            n0++;
        } else {
            if ( n0 > 0 ) {
                nums[i-n0] = nums[i];
            }
        }
    }

    for ( var j = 0; j < n0; j++ ) {
        nums[n-1-j] = 0;
    }

};