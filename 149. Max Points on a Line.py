# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if points is None or len(points) == 0:
            return 0
        dup = {}
        for point in points:
            dup[(point.x, point.y)] = dup.get((point.x, point.y), 0) + 1
        P = dup.keys()
        if len(P) == 1:
            return dup[P[0]]
        result = 0
        for i in xrange(len(P)-1):
            slopes = {}
            for j in xrange(i+1, len(P)):
                dx = P[i][0] - P[j][0]
                dy = P[i][1] - P[j][1]
                if dx == 0:
                    slope = '#'
                elif dy == 0:
                    slope = 0
                else:
                    slope = float(dy)/dx
                slopes[slope] = slopes.get(slope, 0) + dup[P[j]]
            result = max(result, dup[P[i]]+max(slopes.values()))
        return result
