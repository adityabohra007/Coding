class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0:
            return False
        sums = [0] * k
        subsum = sum(nums)/k
        nums = sorted(nums, reverse=True)
        l = len(nums)

        def helper(i):
            if i == l:
                return len(set(sums)) == 1
            for j in xrange(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and helper(i+1):
                    return True
                sums[j] -= nums[i]
                # no need to try other empty bucket
                if sums[j] == 0:
                    break
            return False

        return helper(0)
