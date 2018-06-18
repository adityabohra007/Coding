# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        for interval in intervals:
            if heap:
                if interval.start < heap[0]:
                    heappush(heap, interval.end)
                else:
                    heappop(heap)
                    heappush(heap, interval.end)
            else:
                heappush(heap, interval.end)
        return len(heap)
        