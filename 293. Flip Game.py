class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) == 0:
            return []
        self.result = []
        self.helper(s, 0)
        return self.result

    def helper(self, s, index):
        if index >= len(s) or (index+1) >= len(s):
            return
        if (s[index] == '+' and s[index+1] == '+'):
            tmp = s[:index]+'--'+s[index+2:]
            self.result.append(tmp)
        self.helper(s, index+1)
