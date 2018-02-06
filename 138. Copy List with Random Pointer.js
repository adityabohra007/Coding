/**
 * Definition for singly-linked list with a random pointer.
 * function RandomListNode(label) {
 *     this.label = label;
 *     this.next = this.random = null;
 * }
 */

/**
 * @param {RandomListNode} head
 * @return {RandomListNode}
 */
var copyRandomList = function(head) {
    if ( head == null ) {
        return null;
    }

    var map = new Map();
    var dummyNode = new RandomListNode(0);
    var pre = dummyNode;
    var newNode;

    while ( head != null ) {
        if ( map.has(head) ) {
            newNode = map.get(head);
        } else {
            newNode = new RandomListNode( head.label );
            map.set( head, newNode );
        }
        pre.next = newNode;

        if ( head.random != null ) {
            if ( map.has( head.random ) ) {
                newNode.random = map.get(head.random);
            } else {
                newNode.random = new RandomListNode( head.random.label );
                map.set(head.random, newNode.random);
            }
        }

        pre = newNode;
        head = head.next;
    }

    return dummyNode.next;
};