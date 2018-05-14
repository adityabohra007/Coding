"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

所以说IP地址总共有四段，每一段可能有一位，两位或者三位，范围是[0, 255]，
题目明确指出输入字符串只含有数字，所以当某段是三位时，
我们要判断其是否越界（>255)，还有一点很重要的是，当只有一位时，0可以成某一段，
如果有两位或三位时，像 00， 01， 001， 011， 000等都是不合法的，
所以我们还是需要有一个判定函数来判断某个字符串是否合法。
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        self.result = []
        self.dfs(s, "", 0)
        return self.result

    def dfs(self, s, ip, sub):
        if sub == 4:
            if len(s) == 0:
                self.result.append(ip[1:])
            return

        for i in xrange(1, 4):
            if i <= len(s):
                subString = s[:i]
                if int(subString) <= 255 and (subString[0] != '0'
                                              or len(subString) == 1):
                    self.dfs(s[i:], ip + '.' + subString, sub + 1)
