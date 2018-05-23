class Solution:
    def nthUglyNumber(self, n):
        q = [1]
        n2 = 0
        n3 = 0
        n5 = 0
        
        while len(q) < n:
            v2 = q[n2] * 2
            v3 = q[n3] * 3
            v5 = q[n5] * 5
            
            minV = min(v2, v3, v5)
            if v2 == minV:
                n2 += 1
            if v3 == minV:
                n3 += 1
            if v5 == minV:
                n5 += 1
            q += [minV]
        
        return q[-1]

"""
Version 2:
用heap来解
"""
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        if n <= 1:
            return n
        n -= 1
        k = [2,3,5]
        heap = []
        for i in xrange(3):
            heapq.heappush(heap,(k[i], i))
        
        value = k[0]
        while n > 0:
            value, level = heapq.heappop(heap)
            while level < 3:
                newValue = k[level] * value
                heapq.heappush(heap,(newValue, level))
                level += 1
            n -= 1
        return value         
        