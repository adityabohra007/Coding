class TwoSum(object):
    def __init__(self):
        self.map = {}

    def add(self, number):
        if number in self.map:
            self.map[number] += 1
        else:
            self.map[number] = 1

    def find(self, value):
        for number in self.map:
            if value - number in self.map and (value - number != number
                                               or self.map[number] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)