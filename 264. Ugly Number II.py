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
            
        