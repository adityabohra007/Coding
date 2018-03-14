/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function(arr, k, x) {
    if ( arr == null || arr.length < 2 ) {
        return arr;
    }

    var start = 0;
    var end = arr.length - 1;
    var mid;

    while ( start + 1 < end ) {
        mid = Math.round(( start + end )/2);
        if ( arr[mid] < x ) {
            start = mid;
        } else {
            end = mid;
        }
    }

    var total = 0;
    var result = [];
    while ( start >= 0 && end < arr.length && total < k ) {
        if ( Math.abs(arr[start] - x) <= Math.abs(arr[end] - x) ) {
            result.push(arr[start--]);
        } else {
            result.push(arr[end++]);
        }
        total++;
    }

    while ( start >=0 && total < k ) {
        result.push(arr[start--]);
        total ++;
    }

    while ( end < arr.length && total < k ) {
        result.push(arr[end++]);
        total ++;
    }

    return result.sort(function(a, b){
        return a-b;
    });
};