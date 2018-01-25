/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    var dummy = new ListNode(0);
    dummy.next = head;

    head = dummy;
    while( true ) {
        head = reverseK( head, k );
        if( head == null ) {
            break;
        }
    }

    return dummy.next;

    // head -> n1 -> n2 -> n3 -> n4 -> ..... -> nk -> nk+1
    // head -> nk -> nk-1 -> nk-2 -> ..... -> n2 -> n1 -> nk+1
    // return n1
    function reverseK( head, k ) {
        var nk = head;
        for ( var i = 0; i < k; i++ ) {
            if ( nk == null ) {
                return null;
            }
            nk = nk.next;
        }

        if ( nk == null ) {
            return null;
        }

        // reverse
        var n1 = head.next;
        var nkplus = nk.next;

        var prev = null;
        var curt = n1;

        while ( curt != nkplus ) {
            var tmp = curt.next;
            curt.next = prev;
            prev = curt;
            curt = tmp;
        }

        // connect
        head.next = nk;
        n1.next = nkplus;
        return n1;
    }
};