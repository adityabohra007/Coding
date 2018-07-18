from heapq import *
class Type:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __cmp__(self, other):
        if self.count != other.count:
            return self.count - other.count
        if min(self.word, other.word) == self.word:
            return 1
        else:
            return -1
        
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hash = {}
        for word in words:
            if word in hash:
                hash[word] += 1
            else:
                hash[word] = 1
        
        heap = []
        for word, count in hash.items():
            heappush(heap, Type(word, count))
            if len(heap) > k:
                heappop(heap)
        
        result = []
        while heap:
            result.append(heappop(heap).word)
        result.reverse()
        return result
        
            
        