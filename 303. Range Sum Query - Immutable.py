class NumArray(object):
    def __init__(self, nums):
        array_length = len(nums)
        self.list = [None] * array_length
        if array_length != 0:
            self.list[0] = nums[0]

            for i in xrange(1, array_length):
                self.list[i] = self.list[i - 1] + nums[i]

    def sumRange(self, i, j):
        if i > j or i < 0 or j < 0 or j > len(self.list):
            return 0

        if i == 0:
            return self.list[j]
        else:
            return self.list[j] - self.list[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)