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

"""
Solution 2
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            if result:
                last = result[-1]
                if interval.start <= last.end:
                    result[-1].end = max(last.end, interval.end)
                else:
                    result.append(interval)
            else:
                result.append(interval)
        return result
        
        