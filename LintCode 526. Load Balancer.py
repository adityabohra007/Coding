class LoadBalancer:
    def __init__(self):
        self.server_ids = []
        self.id2index = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id in self.id2index:
            return
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id not in self.id2index:
            return
        index = self.id2index[server_id]
        del(self.id2index[server_id])
        last = self.server_ids[-1]
        self.id2index[last] = index
        self.server_ids[index] = last
        self.server_ids.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        import random
        
        return self.server_ids[random.randint(0,len(self.server_ids) - 1)]
