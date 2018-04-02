"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):

        n1 = 0
        n2 = 0
        ret = []

        while n1 < len(list1) and n2 < len(list2):
            interval1 = list1[n1]
            interval2 = list2[n2]

            if interval1.start < interval2.start:
                self.helper(ret, interval1)
                n1 += 1
            else:
                self.helper(ret, interval2)
                n2 += 1

        while n1 < len(list1):
            self.helper(ret, list1[n1])
            n1 += 1

        while n2 < len(list2):
            self.helper(ret, list2[n2])
            n2 += 1

        return ret

    def helper(self, ret, interval):
        if len(ret) == 0:
            ret.append(interval)
        else:
            lastInterval = ret[-1]
            if lastInterval.end >= interval.start:
                lastInterval.end = max(lastInterval.end, interval.end)
                ret.pop()
                ret.append(lastInterval)
            else:
                ret.append(interval)
