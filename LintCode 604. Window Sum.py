class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        result = []
        if not nums or len(nums) == 0 or k is None or len(nums) < k:
            return result
        v1 = 0
        for n in nums[:k]:
            v1 += n
        result.append(v1)

        for i in xrange(k, len(nums)):
            v = result[i - k] + nums[i] - nums[i - k]
            result.append(v)
        return result