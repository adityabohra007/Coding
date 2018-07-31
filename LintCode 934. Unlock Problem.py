class Solution:
    """
    @param n: the number of keys
    @param m: the number of locks
    @return: the numbers of open locks
    """
    def unlock(self, n, m):
        # Write your code here
        locks = [0]*(m+1)
        for i in xrange(1, n+1):
            p = 1
            while i * p <= m:
                if locks[i*p] == 0:
                    locks[i*p] = 1
                else:
                    locks[i*p] = 0
                p += 1
        return sum(locks)
