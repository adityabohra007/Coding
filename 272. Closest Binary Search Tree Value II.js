/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} target
 * @param {number} k
 * @return {number[]}
 */
/**
 * 中序遍历暴力解法。队没满遇到一个node就塞进去；满了就把距离远的删了，距离近的塞进去。
 */
var closestKValues = function(root, target, k) {

    var result = [];
    inOrder(root, target, k, result);

    return result;
};

var inOrder = function(root, target, k, result) {
    if (!root) {
        return;
    }

    inOrder(root.left, target, k, result);
    if (result.length < k) {
        result.push(root.val);
    } else {
        if (Math.abs(root.val-target) < Math.abs(result[0]-target)) {
            result.shift();
            result.push(root.val);
        }
    }
    inOrder(root.right, target, k, result);
};

