from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if buildings is None or len(buildings) == 0:
            return []
        points = []
        for i in xrange(len(buildings)):
            building = buildings[i]
            points.append((building[0], -building[2], i))
            points.append((building[1], building[2], i))
        points = sorted(points)
        result = []
        h = []
        rightIndex = set([])
        maxHeight = 0
        for i in xrange(len(points)):
            p = points[i]
            if p[1] < 0:
                heappush(h, (p[1], p[2]))
            else:
                rightIndex.add(p[2])
                while h and h[0][1] in rightIndex:
                    heappop(h)

            if not h:
                result.append([p[0], 0])
                maxHeight = 0
            elif maxHeight != -h[0][0]:
                result.append([p[0], -h[0][0]])
                maxHeight = -h[0][0]
        return result

"""
LintCode版本: 要求有点不一样
"""
from heapq import *
class Solution2:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        if buildings is None or len(buildings) == 0:
            return []
        points = []
        for i in xrange(len(buildings)):
            building = buildings[i]
            points.append((building[0], -building[2], i))
            points.append((building[1], building[2], i))
        points = sorted(points)
        result = []
        h = []
        rightIndex = set([])
        maxHeight = 0
        stop = False
        for i in xrange(len(points)):
            p = points[i]
            if p[1] < 0:
                heappush(h, (p[1], p[2]))
            else:
                rightIndex.add(p[2])
                while h and h[0][1] in rightIndex:
                    heappop(h)

            if not h:
                if result and not stop:
                    result[-1][1] = p[0]
                stop = True
                maxHeight = 0
            elif maxHeight != -h[0][0]:
                if result and not stop:
                    result[-1][1] = p[0]
                result.append([p[0], 0, -h[0][0]])
                stop = False
                maxHeight = -h[0][0]
        return result
