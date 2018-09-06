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
        
        
"""
方法二
"""
# class doubleLinkedList(object):

#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.freq = 1
#         self.pre = self.next = None


class LFUCache2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key2node = {}
        self.freq2node = {}
        self.minFreq = 0
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        old_freq = node.freq
        node.freq = old_freq + 1
        self.remove(node, old_freq)
        self.setHead(node, old_freq+1)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity < 1:
            return
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.get(key)
        else:
            node = doubleLinkedList(key, value)
            if self.size >= self.capacity:
                tail = self.freq2node[self.minFreq][1]
                self.remove(tail, self.minFreq)
                del(self.key2node[tail.key])
            self.key2node[key] = node
            self.setHead(node, 1)
            self.minFreq = 1

    def remove(self, node, freq):
        self.size -= 1
        if node.pre:
            node.pre.next = node.next
        else:
            self.freq2node[freq][0] = node.next
        if node.next:
            node.next.pre = node.pre
        else:
            self.freq2node[freq][1] = node.pre
        if self.freq2node[freq][0] is None:
            del(self.freq2node[freq])
            if freq == self.minFreq:
                self.minFreq += 1

    def setHead(self, node, freq):
        self.size += 1
        node.pre = None
        node.next = None
        if freq not in self.freq2node:
            self.freq2node[freq] = [node, node]
            if self.minFreq == 0:
                self.minFreq = freq
        else:
            oldHead = self.freq2node[freq][0]
            node.next = oldHead
            node.pre = None
            oldHead.pre = node
            self.freq2node[freq][0] = node