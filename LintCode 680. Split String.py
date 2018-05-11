"""
Give a string, 
you can choose to split the string after one character or two adjacent characters, 
and make the string to be composed of only one character or two characters. 
Output all possible results.

Example
Given the string "123"
return [["1","2","3"],["12","3"],["1","23"]]
"""
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, p):
        if len(s) == 0:
            self.result.append(p)
            return
        self.dfs(s[1:], p + [s[0]])
        if len(s) > 1:
            self.dfs(s[2:], p + [s[:2]])