INT_MAX = 2147483647
class Memcache:
    def __init__(self):
        self.mem = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key not in self.mem:
            return INT_MAX
        res = self.mem[key]
        if res[1] == -1 or res[1] >= curtTime:
            return res[0]
        return INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        expired = -1
        if ttl:
            expired = curtTime + ttl - 1
        self.mem[key] = [value, expired]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        if key not in self.mem:
            return 
        del(self.mem[key])

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        if self.get(curtTime, key) ==  INT_MAX:
            return INT_MAX
        self.mem[key][0] += delta
        
        return self.mem[key][0]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        if self.get(curtTime, key) ==  INT_MAX:
            return INT_MAX
        self.mem[key][0] -= delta
        
        return self.mem[key][0]
