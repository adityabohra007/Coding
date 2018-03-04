/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    if ( head == null || head.next == null ) {
        return head;
    }

    var mid = findMiddle(head);

    var right = sortList(mid.next);
    mid.next = null;
    var left = sortList(head);

    return merge(left, right);
};

var findMiddle = function(node) {
    var slow = node;
    var fast = node.next;

    while ( fast != null && fast.next != null ) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
};

var merge = function(left, right) {
    var dummy = new ListNode(0);
    var tail = dummy;

    while ( left != null && right != null ) {
        if ( left.val < right.val ) {
            tail.next = left;
            left = left.next;
        } else {
            tail.next = right;
            right = right.next;
        }
        tail = tail.next;
    }

    if ( left != null ) {
        tail.next = left;
    }

    if ( right != null ) {
        tail.next = right;
    }

    return dummy.next;

};