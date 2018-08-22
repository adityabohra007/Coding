class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        m = len(words)
        if m == 0:
            return True
        n = len(words[0])
        if n == 0:
            return True
        if m != n:
            return False
        for i in xrange(m):
            for j in xrange(len(words[i])):
                if j >= m or i >= len(words[j]):
                    return False
                if i < j:
                    if words[i][j] != words[j][i]:
                        return False
        return True
