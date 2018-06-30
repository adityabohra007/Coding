# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in xrange(1, n):
            if knows(result, i):
                result = i
        
        for i in xrange(n):
            if i != result and not knows(i, result):
                return -1
            if i != result and knows(result, i):
                return -1
        return result
        