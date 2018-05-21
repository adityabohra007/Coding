"""
Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

Example

For [1,3,2,3], the previous permutation is [1,2,3,3]

For [1,2,3,4], the previous permutation is [4,3,2,1]
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums
        j = len(nums) - 1
        while j > i and nums[j] >= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

        for j in range(0, (len(nums) - i) // 2):
            nums[i + j + 1], nums[len(nums) - j - 1] = nums[len(nums) - j -
                                                            1], nums[i + j + 1]
        return nums