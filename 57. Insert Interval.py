# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        p = 0
        result = []
        for interval in intervals:
            if interval.end < newInterval.start:
                result.append(interval)
                p += 1
            elif interval.start > newInterval.end:
                result.append(interval)
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        result.insert(p, newInterval)
        return result
            
            
        