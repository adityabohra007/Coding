/**
 * Definition for undirected graph.
 * function UndirectedGraphNode(label) {
 *     this.label = label;
 *     this.neighbors = [];   // Array of UndirectedGraphNode
 * }
 */

/**
 * @param {UndirectedGraphNode} graph
 * @return {UndirectedGraphNode}
 */
var cloneGraph = function(graph) {
    if ( !graph ) {
        return null;
    }

    var queue = [];
    var arr = [];
    queue.push( graph );
    arr[graph.label] = new UndirectedGraphNode( graph.label );

    while ( queue.length > 0 ) {
        var node = queue.shift();
        var newNode = arr[node.label];
        if ( node.neighbors.length > 0 ) {
            for ( var i = 0; i < node.neighbors.length; i++ ) {
                if ( node.label != node.neighbors[i].label ) {
                    var neighbor = node.neighbors[i];
                    var newNeighbor;
                    if ( arr[neighbor.label] ) {
                        newNeighbor = arr[neighbor.label]
                    } else {
                        newNeighbor = new UndirectedGraphNode( node.neighbors[i].label );
                        queue.push( node.neighbors[i] );
                        arr[node.neighbors[i].label] = newNeighbor;
                    }
                    newNode.neighbors.push( newNeighbor );
                } else {
                    newNode.neighbors.push( arr[node.label] );
                }
            }
        }
    }
    return arr[graph.label];
};