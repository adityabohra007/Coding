/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if ( grid == null || grid.length == 0 || grid[0].length == 0 ) {
        return 0
    }

    var m = grid.length;
    var n = grid[0].length;
    var visited = [];
    var island = 0;

    for ( var i = 0; i < m; i++ ) {
        visited[i] = [];
        for ( var j = 0; j < n; j++ ) {
            visited[i][j] = false;
        }
    }

    for ( var i = 0; i < m; i++ ) {
        for ( var j = 0; j < n; j++ ) {
            if ( !visited[i][j] && grid[i][j] == 1 ){
                island ++;
                bfs( grid, visited, i, j );
            }
        }
    }

    return island;

    function bfs ( grid, visited, i, j ) {
        if ( i >= 0 && i < grid.length
            && j >=0 && j < grid[0].length
            && !visited[i][j]
            && grid[i][j] == 1 ) {
            visited[i][j] = true;
            bfs( grid, visited, i - 1, j );
            bfs( grid, visited, i, j - 1 );
            bfs( grid, visited, i + 1, j );
            bfs( grid, visited, i, j + 1 );
        }
    }
};