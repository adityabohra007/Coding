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
var detectCycle = function(head) {

    var slow = head;
    var fast = head;

    while ( true ) {
        if ( fast == null || fast.next == null ) {
            return null;
        }
        slow = slow.next;
        fast = fast.next.next;
        if ( slow == fast ) {
            slow = head;
            while ( true ) {
                if ( slow == fast ) {
                    return slow;
                }
                slow = slow.next;
                fast = fast.next;
            }
        }
    }

};