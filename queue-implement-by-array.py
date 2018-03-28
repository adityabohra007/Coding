class queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def outqueue(self):
        if not self.queue == []:
            self.queue.pop(0)
        else:
            return None
    
    def show(self):
        for i in self.queue:
            print i
    
    def head(self):
        if not self.queue == []:
            return self.queue[0]
        else:
            return None

    def tail(self):
        if not self.queue == []:
            return self.queue[-1]
        else:
            return None
    
    def isEmpty(self):
        return self.queue == []

    def length(self):
        return len(self.queue)


