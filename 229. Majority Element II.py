class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) < 1:
            return []
        self.quickSort(nums, 0, len(nums) - 1)
        cur = nums[0]
        count = 1
        result = []
        n = len(nums) / 3
        for num in nums[1:]:
            if num == cur:
                count += 1
            else:
                if count > n:
                    result.append(cur)
                cur = num
                count = 1
        if count > n:
            result.append(cur)
        return result

    def quickSort(self, nums, start, end):
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
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)

"""
Solution 2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1, c1 = None, 0
        n2, c2 = None, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 += 1
            elif c2 == 0:
                n2 = num
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        result = []
        for num in [n1, n2]:
            if nums.count(num) > len(nums)/3:
                result.append(num)
        return result