class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        nums = list(set(nums))
        self.helper(nums, 0, len(nums)-1)
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]

    def helper(self, nums, start, end):
        if start >= end:
            return
        left = start
        right = end
        pivot = nums[(start+end)/2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.helper(nums, start, right)
        self.helper(nums, left, end)
