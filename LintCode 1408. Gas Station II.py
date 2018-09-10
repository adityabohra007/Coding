from heapq import *


class Solution:
    """
    @param target: The target distance
    @param original: The original gas
    @param distance: The distance array
    @param apply: The apply array
    @return: Return the minimum times
    """

    def getTimes(self, target, original, distance, apply):
        # Write your code here
        heap = []
        result = 0
        cur_distance = 0
        if target > distance[-1]:
            distance.append(target)
            apply.append(0)
        capacity = original
        for i in xrange(len(distance)):
            if distance[i] >= target:
                distance[i] = target
            require_distance = distance[i] - cur_distance
            while capacity < require_distance and len(heap) > 0:
                capacity += heappop(heap)[1]
                result += 1
            if capacity >= require_distance:
                capacity -= require_distance
            else:
                result = -1
                break
            heappush(heap, (-apply[i], apply[i]))
            cur_distance = distance[i]
            if cur_distance >= target:
                break
        return result
