/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function(n, edges) {
    if ( edges.length + 1 != n ) {
        return false;
    }

    var nodes = [];
    for ( var i = 0; i < n; i++ ) {
        nodes[i] = [];
    }

    for ( var j = 0; j < edges.length; j++ ) {
        nodes[edges[j][0]].push( edges[j][1] );
        nodes[edges[j][1]].push( edges[j][0] );
    }

    var arr1 = [];
    var arr2 = [];

    arr1.push( 0 );
    arr2.push( 0 );

    while ( arr1.length > 0 ) {
        var node = arr1.shift();
        var neighbors = nodes[node];
        if ( neighbors.length > 0 ) {
            for ( var k = 0; k < neighbors.length; k++ ) {
                if ( arr2.indexOf( neighbors[k] ) != -1 ) {
                    continue;
                }
                arr1.push(neighbors[k]);
                arr2.push(neighbors[k]);
            }
        }
    }

    return arr2.length == n
};