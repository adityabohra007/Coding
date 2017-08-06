/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
/**
 * 思路：
 （1）题意为将给定的二叉树转化为“只有右孩子节点”的链表（树）。
 （2）由上图可知，如果右子树不为空，则右子树最后肯定为左子树最有一个靠右的孩子节点的右子树，而左子树最后成为整棵树的右子树。这样，首先判断左子树是否为空，不为空就寻找到树根的左孩子节点，然后寻找该节点是否有右孩子，如果有继续寻找，直到找到属于叶子节点的右孩子，此时，该节点的右子树“指向”当前树的右子树，并将当前左子树变为树根的右孩子，将整棵树左孩子置为空。最后，根节点“指向”根节点的右孩子，继续上述操作，直到整棵树遍历完即得到结果。
 */
var flatten = function(root) {

    helper ( root );

    function helper ( root ) {
        if ( !root ) {
            return null;
        }

        var leftPart = helper( root.left );
        var rightPart = helper( root.right );

        if ( leftPart ){
            leftPart.right = root.right;
            root.right = root.left;
            root.left = null;
        }

        // 返回下一个的起点
        if ( rightPart ) {
            return rightPart;
        }

        if ( leftPart ){
            return leftPart;
        }

        return root;
    }
};