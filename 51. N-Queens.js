/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    var result = [];
    if ( n < 0 ) {
        return result;
    }

    dfs( n, result, [] );

    return result;

    function dfs ( n, result, tmp ) {
        if ( tmp.length == n ) {
            result.push ( drawChessBoard(tmp) );
            return;
        }

        for ( var i = 0; i < n; i++ ) {
            if ( !isValid( tmp, i ) ){
                continue;
            }
            tmp.push( i );
            dfs( n, result, tmp );
            tmp.pop();
        }
    }

    function isValid ( tmp, column ) {
        var row = tmp.length;
        for ( var i = 0; i < row; i++ ) {
            if ( tmp[i] == column ) {
                return false;
            }
            if ( i + tmp[i] == row + column ) {
                return false;
            }
            if ( i - tmp[i] == row - column ) {
                return false;
            }
        }

        return true;
    }

    function drawChessBoard ( tmp ) {
        var chessBoard = [];
        for ( var i = 0; i < tmp.length; i++ ) {
            var line = '';
            for ( var j = 0; j < tmp.length; j++ ) {
                if ( j == tmp[i] ) {
                    line += 'Q';
                } else {
                    line += '.';
                }
            }
            chessBoard.push(line);
        }
        return chessBoard;
    }
};