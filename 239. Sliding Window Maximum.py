class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []
        if len(nums) < k:
            return [max(nums)]

        result = []
        q = nums[:k]
        m = max(q)
        result.append(m)
        for i in xrange(k, len(nums)):
            f = False
            if nums[i] > m:
                m = nums[i]
            elif m == q[0]:
                f = True
            q.pop(0)
            q.append(nums[i])
            if f:
                m = max(q)
            result.append(m)
        return result


"""
Solution 2
"""
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        result = []
        if len(nums) < k or k == 0:
            return result
        
        for i in xrange(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            if i < k - 1:
                continue
            
            while q and q[0] <= i - k:
                q.popleft()
            result.append(nums[q[0]])
        return result