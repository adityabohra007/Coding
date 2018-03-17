/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    if ( nums === null || nums.length === 0 ) {
        return null;
    }

    quickSort(nums, 0, nums.length-1);
};

var quickSort = function(nums, left, right) {
    if ( left >= right ) {
        return;
    }

    var mid = nums[Math.floor((left+right)/2)];
    var l = left;
    var r = right;

    while ( l <= r ) {
        while ( l <= r && nums[l] < mid ) {
            l++;
        }
        while ( l <= r && nums[r] > mid ) {
            r--;
        }
        if ( l <= r ) {
            var tmp = nums[l];
            nums[l] = nums[r];
            nums[r] = tmp;

            l++;
            r--;
        }
    }

    quickSort(nums, left, r);
    quickSort(nums, l, right);
}