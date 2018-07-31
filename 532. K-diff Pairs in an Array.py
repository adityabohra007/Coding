class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) < 2 or k < 0:
            return 0
        hash = {}
        result = 0
        for num in nums:
            if k == 0:
                if num in hash and hash[num] == 1:
                    result += 1
            else:
                if num not in hash and num-k in hash:
                    result += 1
                if num not in hash and num+k in hash:
                    result += 1
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        return result
