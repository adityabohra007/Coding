import heapq


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        heapq.heapify(nums)

        topk = heapq.nlargest(k, nums)
        sorted(topk, reverse=True)
        return topk