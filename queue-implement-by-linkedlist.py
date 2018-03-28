class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, val):
        node = Node(val)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    
    def outqueue(self):
        if (self.first == None):
            return None
        else:
            tmp = self.first
            self.first = self.first.next
            return tmp
    
    def outallqueue(self):
        list = []
        while self.first is not None:
            list.append(self.first.val)
            self.first = self.first.next
        return list


