class Solution(object):
    def findKthLargest(self, nums, k):
        self.quickSort(nums, 0, len(nums) - 1, k)
        return nums[-k]

    def quickSort(self, A, start, end, k):
        if start >= end:
            return

        left = start
        right = end
        pivot = A[(start + end) / 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        if left <= len(A) - k:
            self.quickSort(A, left, end, k)
        else:
            self.quickSort(A, start, right, k)
