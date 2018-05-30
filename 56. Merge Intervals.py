# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        self.result = []
        for interval in intervals:
            self.helper(interval)
        return self.result
    
    def helper(self, interval):
        if len(self.result) == 0:
            self.result.append(interval)
        else:
            lastInterval = self.result[-1]
            if lastInterval.end >= interval.start:
                lastInterval.end = max(lastInterval.end, interval.end)
                self.result.pop()
                self.result.append(lastInterval)
            else:
                self.result.append(interval)
        