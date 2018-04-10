from pprint import pprint
import sys

class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        n = self.getTotal(nums)

        if n == 0:
            return 0.00

        if n % 2 != 0:
            return findKth(nums, n / 2 + 1) / 1.00
        else:
            return (findKth(nums, n / 2 + 1) + findKth(nums, n / 2)) / 2.00

    def getTotal(self, nums):
        sum = 0
        for num in nums:
            sum += len(num)
        return sum

    def findKth(self, nums, k):
        start = 0
        end = sys.maxint

        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if self.getGTE(nums, mid) >= k:
                start = mid
            else:
                end = mid

        if self.getGTE(nums, start) >=k:
            return start
        else:
            return end

    def getGTE(self, nums, k):
        sum = 0
        for num in nums:
            sum += self.getGTK(num, k)

        return sum

    def getGTK(self, num, k):
        if num is None or len(num) == 0:
            return 0

        start = 0
        end = len(num) - 1

        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if num[mid] >= k:
                end = mid
            else:
                start = mid
        
        if num[start] >= k:
            return len(num) - start
        
        if num[end] >= k:
            return len(num) - end
        
        return 0

