import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val in self.pos:
            index = self.pos[val]
            last = self.nums[-1]
            self.nums[index] = last
            self.pos[last] = index
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
Version 2: Python 2
"""


class RandomizedSet(object):
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val not in self.pos:
            return False
        valIndex = self.pos[val]
        lastIndex = len(self.nums) - 1
        self.nums[valIndex], self.nums[lastIndex] = self.nums[
            lastIndex], self.nums[valIndex]
        self.pos[self.nums[valIndex]] = valIndex
        self.nums.pop()
        self.pos.pop(val)
        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()