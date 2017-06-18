/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if( matrix == null || matrix.length == 0 ) {
        return false;
    }

    for ( var arr of matrix ) {
        var result = binarySearch( arr, target );
        if ( result ) {
            return true;
        }
    }
    return false;

    function binarySearch( arr, target ) {
        if( arr == null || arr.length == 0 ) {
            return false;
        }

        var mid;
        var start = 0;
        var end = arr.length -1;

        while ( start + 1 < end ) {
            mid = start + Math.round(( end - start ) / 2);
            if ( arr[mid] == target ) {
                return true;
            } else if( arr[mid] > target ) {
                end = mid;
            } else {
                start = mid;
            }
        }

        if ( arr[start] == target || arr[end] == target ) {
            return true;
        }

        return false;
    }
};