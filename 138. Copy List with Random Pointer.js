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
var copyRandomListII = function(head) {

    if ( head == null ) {
        return head;
    }

    var map = new Map();
    var newHead = new RandomListNode(head.label);
    map.set(head, newHead);
    var pre = newHead;
    var node = head.next;

    while ( node != null ) {
        var newNode = new RandomListNode(node.label);
        map.set(node, newNode);
        pre.next = newNode;
        pre = newNode;
        node = node.next;
    }

    node = head;
    var copyNode = newHead;

    while ( node != null ) {
        if ( node.random != null ) {
            copyNode.random = map.get(node.random);
        }
        copyNode = copyNode.next;
        node = node.next;
    }

    return newHead;
};