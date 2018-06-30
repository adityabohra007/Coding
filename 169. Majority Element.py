class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 1:
            return None
        cur = nums[0]
        count = 1
        for num in nums[1:]:
            count += 1 if num == cur else -1
            if count == 0:
                cur = num
                count += 1
        return cur
