var linkedNode = function(key, value) {
    this.key = key;
    this.value = value;
    this.pre = this.next = null;
};
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.hash = new Map();
    this.head = null;
    this.tail = null;
};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (this.hash.has(key)) {
        var node = this.hash.get(key);
        this.remove(node);
        this.setHead(node);
        return node.value;
    } else {
        return -1;
    }
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.hash.has(key)) {
        var oldNode = this.hash.get(key);
        oldNode.value = value
        this.remove(oldNode);
        this.setHead(oldNode);
    } else {
        var newNode = new linkedNode(key, value);
        if (this.hash.size >= this.capacity) {
            this.hash.delete(this.tail.key);
            this.remove(this.tail);
            this.setHead(newNode);
        } else {
            this.setHead(newNode);
        }
        this.hash.set(key, newNode);
    }
};

LRUCache.prototype.remove = function(node) {
    if (node.pre) {
        node.pre.next = node.next;
    } else {
        this.head = node.next;
    }

    if (node.next) {
        node.next.pre = node.pre;
    } else {
        this.tail = node.pre;
    }
};

LRUCache.prototype.setHead = function(node) {
    node.next = this.head;
    node.pre = null;

    if (this.head) {
        this.head.pre = node;
    }

    this.head = node;

    if (!this.tail) {
        this.tail = this.head;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = Object.create(LRUCache).createNew(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */