function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var preOrder = function( node ) {
    var result = [];

    if ( !node ) {
        return result;
    }

    result.push(node);
    preOrder(node.left);
    preOrder(node.right);

    return result;
};

var inOrder = function ( node ) {
    var result = [];

    if ( !node ) {
        return result;
    }

    inOrder(node.left);
    result.push(node);
    inOrder(node.left);

    return result;
};

var postOrder = function ( node ) {
    var result = [];

    if ( !node ) {
        return result;
    }

    postOrder(node.left);
    postOrder(node.right);
    result.push(node);

    return result;
};