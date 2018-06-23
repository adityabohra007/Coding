"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
from heapq import *
class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and 
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        # Write your your code here
        node = self.root
        for c in word:
            child = node.children.get(c, None)
            if child is None:
                child = TrieNode()
                node.children[c] = child
            child.top10 = self.update(child.top10, frequency)
            node = child
    
    def update(self, top10, f):
        heappush(top10, f)
        if len(top10) > 10:
            heappop(top10)
        top10 = sorted(top10, reverse=True)
        return top10
       


