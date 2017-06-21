/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if ( matrix == null || matrix.length == 0 ) {
        return false;
    }

    if ( matrix[0] == null || matrix[0].length == 0 ) {
        return false;
    }

    var n = matrix.length;
    var m = matrix[0].length;
    var x = n - 1;
    var y = 0;
    var count = 0;

    while ( x >= 0 && y < m ) {
        if( matrix[x][y] > target ) {
            x--;
        } else if ( matrix[x][y] < target ) {
            y++;
        } else {
            count ++;
            x--;
            y++
        }
    }

    if ( count > 0 ) {
        return true;
    } else {
        return false;
    }
};