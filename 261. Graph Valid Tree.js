/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function(n, edges) {
    if ( n == 0 ) {
        return false;
    }

    if ( n != (edges.length + 1) ) {
        return false;
    }

    // initial graph
    var graph = [];
    for ( var i = 0; i < n; i++ ) {
        graph[i] = [];
    }

    for ( var j = 0; j < edges.length; j++ ) {
        var u = edges[j][0];
        var v = edges[j][1];

        graph[u].push( v );
        graph[v].push( u );
    }

    // validation
    var arr1 = [];
    var arr2 = [];

    arr1.push(0);
    arr2.push(0);

    while ( arr1.length > 0 ) {
        var node = arr1.shift();
        var neighbors = graph[node];
        if ( neighbors != -1 && neighbors.length > 0 ) {
            for ( var i = 0; i < neighbors.length; i++ ) {
                if ( arr2.indexOf( neighbors[i] ) != -1 ) {
                    continue;
                }
                arr1.push( Number(neighbors[i]) );
                arr2.push( Number(neighbors[i]) );
            }
        }
        graph[node] = -1;
    }

    return arr2.length == n;
};