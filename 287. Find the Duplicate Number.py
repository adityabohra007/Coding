class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            k = nums[i] - 1
            if nums[i] != i + 1:
                if nums[k] == nums[i]:
                    return nums[i]
                else:
                    nums[i], nums[k] = nums[k], nums[i]
            else:
                i += 1
        return None


"""
solution 2: 用类似linked list的方法
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return slow