class Node:    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.insert(node)
        else:
            return False
        
class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        node = Node(start, end)
        if self.root:
            return self.root.insert(node)
        else:
            self.root = node
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)