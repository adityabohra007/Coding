class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or m == 0:
            return 0
        lo = max(nums)
        hi = sum(nums)

        while lo + 1 < hi:
            largest_sum = (lo + hi) / 2
            if self.helper(nums, m, largest_sum):
                hi = largest_sum
            else:
                lo = largest_sum
        if self.helper(nums, m, lo):
            return lo
        return hi

    def helper(self, nums, m, largest_sum):
        num_of_sub = 0
        current_sum = 0

        for num in nums:
            if num + current_sum <= largest_sum:
                current_sum += num
            else:
                num_of_sub += 1
                current_sum = num
        num_of_sub += 1
        return num_of_sub <= m
