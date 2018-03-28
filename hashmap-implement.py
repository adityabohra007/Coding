class HashMap(object):

    def __init__(self, length = 10):
        self.length = length
        self.items = [[]for i in range(self.length)]
    
    def hash(self, key):
        # 计算该key在items哪个list中，针对不同类型的key需重新实现
        return key % self.length
    
    def equals(self, key1, key2):
        return key1 == key2
    
    def insert(self, key, value):
        index = self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key, item[0]):
                    self.items[index].remove(item)

        self.items[index].append((key, value))
    
    def get(self, key):
        index = self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key, item[0]):
                    return item[1]
        # 找不到key，则抛出KeyError异常
        raise KeyError
    
    def __setitem__(self, key, value):
        """支持以 myhash[1] = 30000 方式添加"""
        return self.insert(key, value)

    def __getitem__(self, key):
        """支持以 myhash[1] 方式读取"""    
        return self.get(key)
