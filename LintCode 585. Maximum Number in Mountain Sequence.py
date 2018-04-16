class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        if not nums or len(nums) == 0:
            return 0

        l = 0
        h = len(nums) - 1

        while l + 1 < h:
            m = (l + h) / 2
            if nums[m] <= nums[m + 1]:
                l = m
            else:
                h = m

        return max(nums[l], nums[h])
