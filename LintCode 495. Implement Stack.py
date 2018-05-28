from collections import deque
class Stack:
    def __init__(self):
        self.q = deque([])
        
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.q.append(x)

    """
    @return: nothing
    """
    def pop(self):
        self.q.pop()

    """
    @return: An integer
    """
    def top(self):
        item = self.q.pop()
        self.push(item)
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.q) == 0
