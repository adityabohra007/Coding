"""
Given a stream of integers and a window size, 
calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
from Queue import Queue
class MovingAverage(object):

    def __init__(self, size):
        self.q = Queue()
        self.size = size
        self.sum = 0

    def next(self, val):
        self.sum += val
        if self.q.qsize() == self.size:
            self.sum -= self.q.get()
        self.q.put(val)
        return self.sum * 1.0 / self.q.qsize()



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)