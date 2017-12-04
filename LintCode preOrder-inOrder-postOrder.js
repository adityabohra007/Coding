function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

//-----------------------------------------------------------------------
var preOrder1 = function( root ) {
    var result = [];

    if ( root ) {
        traverse( root, result );
    }

    return result;

    function traverse( node, result ) {
        if ( !node ) {
            return;
        }
        result.push( node.val );
        traverse( node.left, result );
        traverse( node.right, result );
    }
};

// Another preOrder
var preOrder2 = function ( root ) {
    var result = [];
    var stack = [];

    if ( !root ) {
        stack.push( root );
    }

    while ( stack.length > 0 ) {
        var node = stack.shift();
        result.push( node.val );
        if ( !node.left ) {
            stack.push( node.left );
        }
        if ( !node.right ) {
            stack.push( node.right );
        }
    }

    return result;
};

//-----------------------------------------------------------------------
var inOrder = function ( root ) {
    var result = [];

    if ( root ) {
        traverse( root, result );
    }

    return result;

    function traverse( node, result ) {
        if ( !node ) {
            return;
        }

        if ( node.left ) {
            traverse( node.left, result );
        }
        result.push( node.val );
        if ( node.right ) {
            traverse( node.right, result );
        }
    }

};

//-----------------------------------------------------------------------
var postOrder = function ( root ) {
    var result = [];

    if ( root ) {
        traverse( root, result );
    }

    return result;

    function traverse( node, result ) {
        if ( !node ) {
            return;
        }

        if ( node.left ) {
            traverse( node.left, result );
        }

        if ( node.right ) {
            traverse( node.right, result );
        }

        result.push( node.val );
    }
};