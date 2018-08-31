class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.result = []
        self.helper(S, "")
        return self.result

    def helper(self, s, tmp):
        if len(s) == 0:
            self.result.append(tmp)
            return
        i = 0
        while i < len(s) and s[i].isdigit():
            tmp += str(s[i])
            i += 1
        if i != len(s):
            self.helper(s[i+1:], tmp+s[i].upper())
            self.helper(s[i+1:], tmp+s[i].lower())
        else:
            self.helper(s[i+1:], tmp)
