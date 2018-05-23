"""
pop()方法中，不要遗漏了self.q1.get()
"""
from Queue import Queue
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.q1.put(x)

    """
    @return: nothing
    """
    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        self.q1.get()
        self.q1, self.q2 = self.q2, self.q1

    """
    @return: An integer
    """
    def top(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        item = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        self.push(item)
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.q1.empty()
