class Node:
    def __init__(self, _val, _pos):
        self.val = _val
        self.pos = _pos

    def __cmp__(self, other):
        if self.val != other.val:
            return self.val - other.val
        return self.pos - other.pos


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        arr = []
        arr.append(Node(0, -1))
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            arr.append(Node(sum, i))
        arr = sorted(arr)

        result = [0, 0]
        import sys
        ans = sys.maxint
        for j in xrange(len(arr) - 1):
            diff = arr[j + 1].val - arr[j].val
            if diff < ans:
                result[0] = min(arr[j + 1].pos, arr[j].pos) + 1
                result[1] = max(arr[j + 1].pos, arr[j].pos)
                ans = diff
        return result