from heapq import heappop, heappush


class Solution:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        self.k = k
        self.nums = []

    """
    @param: num: Number to be added
    @return: nothing
    """

    def add(self, num):
        heappush(self.nums, num)
        if len(self.nums) > self.k:
            heappop(self.nums)

    """
    @return: Top k element
    """

    def topk(self):
        # write your code here
        return sorted(self.nums, reverse=True)