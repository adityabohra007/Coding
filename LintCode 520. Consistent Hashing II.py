class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        solution = cls()
        solution.n = n
        solution.k = k
        solution.ids = {}
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        import random
        result = []
        for _ in xrange(self.k):
            i = random.randint(0, self.n-1)
            while i in self.ids:
                i = random.randint(0, self.n-1)
            result.append(i)
            self.ids[i] = machine_id
        result = sorted(result)
        return result

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        import bisect
        idArr = self.ids.keys()
        idArr = sorted(idArr)
        index = bisect.bisect_left(idArr, hashcode)
        if index >= len(idArr):
            id = idArr[0]
        else:
            id = idArr[index]
        return self.ids[id]
        
"""
引入self.machines = {}
"""
class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        solution = cls()
        solution.n = n
        solution.k = k
        solution.ids = {}
        solution.machines = {}
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        import random
        result = []
        for _ in xrange(self.k):
            i = random.randint(0, self.n-1)
            while i in self.ids:
                i = random.randint(0, self.n-1)
            result.append(i)
            self.ids[i] = machine_id
        result = sorted(result)
        self.machines[machine_id] = result
        return result

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        import bisect
        id = -1
        distance = self.n + 1
        for k, v in self.machines.items():
            i = bisect.bisect_left(v, hashcode) % len(v)
            d = v[i] - hashcode
            if d < 0:
                d += self.n
            if d < distance:
                distance = d
                id = k
        return id
        
