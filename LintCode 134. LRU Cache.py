"""
LRU是Least Recently Used的缩写，即最近最久未使用，常用于页面置换算法，是为虚拟页式存储管理服务的。
内存管理的一种页面置换算法，对于在内存中但又不用的数据块（内存块）叫做LRU，操作系统会根据哪些数据属于LRU而将其移出内存而腾出空间来加载另外的数据。
"""
class LinkedNode:
    
    def __init__(self, key=None, value=None, pre = None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next
        
class LRUCache:
    
    def __init__(self, capacity):
        self.hash = {}
        self.head = None
        self.tail = self.head
        self.capacity = capacity

    def get(self, key):
        if key not in self.hash:
            return -1
        else:
            n = self.hash[key]
            self.remove(n)
            self.setHead(n)
            return n.value

    def set(self, key, value):
        if key in self.hash:
            n = self.hash[key]
            n.value = value
            self.remove(n)
            self.setHead(n)
        else:
            n = LinkedNode(key, value)
            if len(self.hash) >= self.capacity:
                del(self.hash[self.tail.key])
                self.remove(self.tail)
                self.setHead(n)
            else:
                self.setHead(n)
            self.hash[key] = n
    
    def remove(self, n):
        if n.pre is not None:
            n.pre.next = n.next
        else:
            self.head = n.next
        
        if n.next is not None:
            n.next.pre = n.pre
        else:
            self.tail = n.pre
    
    def setHead(self, n):
        n.next = self.head
        n.pre = None
        
        if self.head is not None:
            self.head.pre = n
        
        self.head = n
        
        if self.tail is None:
            self.tail = self.head
            

