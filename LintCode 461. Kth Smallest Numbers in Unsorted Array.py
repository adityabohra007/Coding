class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        self.quickSort(nums, 0, len(nums) - 1, k)
        return nums[k - 1]

    def quickSort(self, nums, start, end, k):
        if start >= end:
            return

        left = start
        right = end
        pivot = nums[(start + end) / 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if left >= k:
            self.quickSort(nums, start, right, k)
        if left < k:
            self.quickSort(nums, left, end, k)
