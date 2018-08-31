class MyCalendarTwo(object):

    def __init__(self):
        self.calendars = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for ov in self.overlaps:
            if start < ov[1] and end > ov[0]:
                return False
        for cl in self.calendars:
            if start < cl[1] and end > cl[0]:
                self.overlaps.append([max(start, cl[0]), min(end, cl[1])])
        self.calendars.append([start, end])
        return True
            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)