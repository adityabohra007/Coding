"""
Implement next permutation, which rearranges numbers into the 
lexicographically next greater permutation of numbers.

If such arrangement is not possible, 
it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. 
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
"""
有如下的一个数组
1　　2　　7　　4　　3　　1
下一个排列为：
1　　3　　1　　2　　4　　7
那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，
数字逐渐变大，到了2时才减小的，然后我们再从后往前找第一个比2大的数字，
是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：

1　　2　　7　　4　　3　　1

1　　2　　7　　4　　3　　1

1　　3　　7　　4　　2　　1

1　　3　　1　　2　　4　　7
"""
"""
在lintcode中，最开始要加上
if list(reversed(sorted(nums))) == nums:
    nums.sort()
    return
才能ac
"""
import sys
class Solution(object):
    def nextPermutation(self, nums):
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                j = len(nums) - 1
                while nums[i] >= nums[j]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                self.quickSort(nums, i + 1, len(nums) - 1)
                return
        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, A, start, end):
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
            self.quickSort(A, left, end)
            self.quickSort(A, start, right)