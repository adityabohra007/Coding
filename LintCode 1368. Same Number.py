class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """

    def sameNumber(self, nums, k):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 'NO'
        hash = {}
        for i in xrange(len(nums)):
            num = nums[i]
            if num in hash:
                if i - hash[num] < k:
                    return 'YES'
            hash[num] = i
        return 'NO'
