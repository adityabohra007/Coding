class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for i in xrange(2, n+1):
            result = self.helper(result)
        return result

    def helper(self, s):
        tmp = ''
        cur = '#'
        count = 0
        for n in s:
            if n != cur:
                if cur != '#':
                    tmp += str(count) + cur
                cur = n
                count = 1
            else:
                count += 1
        tmp += str(count) + cur
        return tmp
