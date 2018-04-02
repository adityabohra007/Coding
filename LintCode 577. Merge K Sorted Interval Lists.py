"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        result = []
        heap = []
        for index, interval in enumerate(intervals):
            if len(interval) == 0:
                continue
            heapq.heappush(
                heap,
                (interval[0].start, interval[0].end, index, 0, interval[0]))

        while len(heap) > 0:
            start, end, row, column, point = heapq.heappop(heap)
            if len(result) == 0:
                result.append(point)
            else:
                lastPoint = result[-1]
                if lastPoint.end >= start:
                    lastPoint.end = max(lastPoint.end, end)
                    result.pop()
                    result.append(lastPoint)
                else:
                    result.append(point)

            if column + 1 < len(intervals[row]):
                heapq.heappush(heap, (intervals[row][column + 1].start,
                                      intervals[row][column + 1].end, row,
                                      column + 1, intervals[row][column + 1]))

        return result