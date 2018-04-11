"""
超时做法
"""
class NumArray_1(object):

    def __init__(self, nums):
        lenN = len(nums)
        self.n = nums
        self.l = [None] * lenN
        if lenN != 0:
            self.l[0] = nums[0]

            for i in xrange(1, lenN):
                self.l[i] = self.l[i - 1] + nums[i]


    def update(self, i, val):
        diff = val - self.n[i]
        self.n[i] = val

        for x in xrange(i, len(self.l)):
            self.l[x] += diff


    def sumRange(self, i, j):
        if i > j or i < 0 or j < 0 or j > len(self.l):
            return 0

        if i == 0:
            return self.l[j]
        else:
            return self.l[j] - self.l[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

"""
AC: 用binary indexed tree
"""


class NumArray_2(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.btree = [0 for x in xrange(self.n)]

        for i in xrange(self.n):
            x = i + 1
            while x <= self.n:
                self.btree[x - 1] += nums[i]
                x += self.lowbit(x)

    def update(self, i, val):
        diff = val - (self.sumbtree(i) - self.sumbtree(i - 1))
        x = i + 1
        while x <= self.n:
            self.btree[x - 1] += diff
            x += self.lowbit(x)

    def sumRange(self, i, j):
        return self.sumbtree(j) - self.sumbtree(i - 1)

    def sumbtree(self, m):
        sum = 0
        x = m + 1
        while x > 0:
            sum += self.btree[x - 1]
            x -= self.lowbit(x)

        return sum

    def lowbit(self, x):
        return x & -x


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)