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

"""
Solution 2: Using Binary index tree
"""
class NumArray(object):

    def __init__(self, nums):
        n = len(nums)
        self.btree = [0 for _ in xrange(n)]
        
        for i in xrange(n):
            x = i+1
            while x <= n:
                self.btree[x-1] += nums[i]
                x += self.lowbit(x)

    def sumRange(self, i, j):
        return self.sum(j) - self.sum(i-1)
        
    def sum(self, n):
        x = n + 1
        sum = 0
        while x > 0:
            sum += self.btree[x-1]
            x -= self.lowbit(x)
        return sum
    
    def lowbit(self, x):
        return x & -x
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)