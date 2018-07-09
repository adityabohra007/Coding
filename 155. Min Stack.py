class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        if len(self.min) == 0 or self.min[-1] >= x:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.s) > 0:
            num = self.s.pop()
            if num == self.min[-1]:
                self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.s) > 0:
            return self.s[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()