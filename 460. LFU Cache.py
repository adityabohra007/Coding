class doubleLinkedList:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.freq = 0
        self.pre = self.next = None
        
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key2node = {}
        self.freq2node = {}
        self.count = 0
        self.minFreq = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        oldFreq = node.freq
        node.freq += 1
        op = self.freq2node[oldFreq]
        # op[0] -> head   op[1] -> tail
        if node.pre is None:
            op[0] = node.next
        else:
            node.pre.next = node.next
        if node.next is None:
            op[1] = node.pre
        else:
            node.next.pre = node.pre
        if op[0] is None:
            del(self.freq2node[oldFreq])
            if oldFreq == self.minFreq:
                self.minFreq += 1
        node.pre = None
        node.next = None
        self.addNode2Freq(node, oldFreq+1)
        return node.value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity < 1:
            return
        if key in self.key2node:
            self.key2node[key].value = value
            self.get(key)
        else:
            if self.count == self.capacity:
                delNode = self.freq2node[self.minFreq][0]
                delNodeKey = delNode.key
                del(self.key2node[delNodeKey])
                if delNode.next is None:
                    del(self.freq2node[self.minFreq])
                else:
                    self.freq2node[self.minFreq][0] = delNode.next
                    self.freq2node[self.minFreq][0].pre = None
            else:
                self.count += 1
            self.minFreq = 0
            newNode = doubleLinkedList(key, value)
            self.key2node[key] = newNode
            self.addNode2Freq(newNode, 0)
    
    def addNode2Freq(self, node, freq):
        if freq in self.freq2node:
            oldEndNode = self.freq2node[freq][1]
            oldEndNode.next = node
            node.pre = oldEndNode
            self.freq2node[freq][1] = node
        else:
            self.freq2node[freq] = [node, node]
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)