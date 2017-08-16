/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    if ( !root ) {
        return '[]';
    }

    var queue = [];
    var index = 0;
    queue.push( root );

    // push all binary tree elements into queue
    while ( index < queue.length ) {
        if ( queue[index] ) {
            queue.push( queue[index].left );
            queue.push( queue[index].right );
        }
        index ++;
    }

    // clean queue from the end
    while ( !queue[ queue.length - 1] ) {
        queue.pop();
    }

    // generate string
    var result = '[';
    result += queue[0].val;
    for ( var i = 1; i < queue.length; i++ ) {
        if ( !queue[i] ) {
            result += ',#';
        } else {
            result += ',' + queue[i].val;
        }
    }
    result += ']';

    return result;

};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    if ( data == '[]' ) {
        return null;
    }

    var serializedArray = data.slice( 1, data.length-1 ).split(',');

    var root = new TreeNode(parseInt(serializedArray[0]));
    var index = 0
    var queue = [];
    queue.push( root );

    for ( var i = 1; i < serializedArray.length; i++ ) {
        if ( serializedArray[i] != '#' ) {
            var node = new TreeNode(parseInt(serializedArray[i]));
            if ( (i+1) % 2 == 0 ) {
                queue[index].left = node
            } else {
                queue[index].right = node
            }
            queue.push( node );
        }
        if ( (i+1) % 2 != 0 ) {
            index ++;
        }
    }

    return root;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */