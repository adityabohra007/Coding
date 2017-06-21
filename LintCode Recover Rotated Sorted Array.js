var recoverRotatedSortedArray = function (nums) {
    if ( nums == null || nums.length == 0 ) {
        return [];
    }

    for ( var index = 0; index < nums.length - 1; index++ ) {
        if ( nums[index] > nums[index+1] ) {
            reverseArray(0, index, nums);
            reverseArray(index+1, nums.length-1, nums);
            reverseArray(0, nums.length-1, nums);
        }
    }
    return nums;

    function reverseArray(start, end, arr) {
        for ( var i = start, j = end; i < j; i++, j-- ) {
            var temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
};