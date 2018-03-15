/*
 * 不是直接改变 nums 的值
 */
var MergeSort_1 = function (nums) {

    var result = [];
    if ( nums == null || nums.length == 0 ) {
        return result;
    }

    result = mergeSort(nums, 0, nums.length-1);

    return result;
};

var mergeSort = function (arr, start, end) {
    if ( start >= end ) {
        return [arr[start]];
    }
    var mid = parseInt( (start+end)/2 );
    var leftPart = mergeSort(arr, start, mid);
    console.log(leftPart);
    var rightPart = mergeSort(arr, mid+1, end);
    return mergeTwoParts(leftPart, rightPart);

};

var mergeTwoParts = function (leftPart, rightPart) {
    var m = leftPart.length - 1;
    var n = rightPart.length - 1;
    var l = m + n + 1;

    while ( m >= 0 && n >= 0 ) {
        if ( leftPart[m] < rightPart[n] ) {
            leftPart[l--] = rightPart[n--];
        } else {
            leftPart[l--] = leftPart[m--];
        }
    }

    while ( n >= 0 ) {
        leftPart[l--] = rightPart[n--];
    }

    return leftPart;

};