class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        length = len(nums)
        has_less = [False for _ in xrange(length)]
        small = nums[0]
        for i in xrange(length):
            if nums[i] > small:
                has_less[i] = True
            else:
                small = nums[i]
        big = nums[-1]
        for i in xrange(length - 1, 0, -1):
            if has_less[i] == True:
                if nums[i] < big:
                    return True
            if nums[i] > big:
                big = nums[i]
        return False
