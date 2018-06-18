from heapq import *
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] -= 1
            else:
                d[num]  = 0
        heap = []
        for key, value in d.items():
            heappush(heap, (value, key))
        result = []
        while len(result) < k:
            point = heappop(heap)
            result.append(point[1])
        return result
        
        