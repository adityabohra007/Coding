import Queue


class MyStack(object):
    def __init__(self):
        self.q1 = Queue.Queue()
        self.q2 = Queue.Queue()

    def push(self, x):
        self.q1.put(x)

    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        item = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return item

    def top(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        item = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        self.push(item)
        return item

    def empty(self):
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()