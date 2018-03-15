/*
 * 直接改变 nums 的值
 */
var MergeSort_2 = function (A) {
    var tmp = new Array(A.length);
    mergeSort(A, 0, A.length-1, tmp);

    return A;
};

var mergeSort = function (arr, start, end, tmp) {
    if ( start >= end ) {
        return;
    }

    var mid = parseInt( (start+end)/2 );

    mergeSort(arr, start, mid, tmp);
    mergeSort(arr, mid+1, end, tmp);
    mergeTwoParts(arr, start, mid, end, tmp);
};

var mergeTwoParts = function (arr, start, mid, end, tmp) {

    var left = start;
    var right = mid+1;
    var index = start;

    // merge two sorted subarray in A to tmp array
    while ( left <= mid && right <= end ) {
        if ( arr[left] < arr[right] ) {
            tmp[index++] = arr[left++];
        } else  {
            tmp[index++] = arr[right++];
        }
    }

    while ( left <= mid ) {
        tmp[index++] = arr[left++];
    }

    while ( right <= end ) {
        tmp[index++] = arr[right++];
    }

    for ( var i = 0; i <= end; i++ ) {
        arr[i] = tmp[i];
    }
};