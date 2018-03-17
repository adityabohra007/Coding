/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    if ( nums === null || nums.length === 0 ) {
        return null;
    }

    quickSort(nums, 0, nums.length - 1);

    return nums[nums.length-k];
};

var quickSort = function(nums, left, right) {

    if ( left >= right ) {
        return;
    }

    var l = left;
    var r = right;
    var tmp
    var pivot = nums[Math.floor((left+right)/2)];

    while ( l <= r ) {
        while ( l <= r && nums[l] < pivot ) {
            l++;
        }
        while ( l <= r && nums[r] > pivot ) {
            r--
        }
        if ( l <= r ) {
            tmp = nums[l];
            nums[l] = nums[r];
            nums[r] = tmp;

            l++;
            r--;
        }
    }

    quickSort(nums, left, r);
    quickSort(nums, l, right);
};