"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, 
your answer could be in any order you want.
"""
class Solution(object):
    def letterCombinations(self, digits):
        map = {}
        map['2'] = ['a', 'b', 'c']
        map['3'] = ['d', 'e', 'f']
        map['4'] = ['g', 'h', 'i']
        map['5'] = ['j', 'k', 'l']
        map['6'] = ['m', 'n', 'o']
        map['7'] = ['p', 'q', 'r', 's']
        map['8'] = ['t', 'u', 'v']
        map['9'] = ['w', 'x', 'y', 'z']

        self.result = []
        self.dfs(digits, map, '', 0)
        return self.result

    def dfs(self, digits, map, tmp, index):
        if len(tmp) == len(digits):
            if len(tmp) > 0:
                self.result.append(tmp[:])
            return
        for c in map[digits[index]]:
            self.dfs(digits, map, tmp + c, index + 1)
