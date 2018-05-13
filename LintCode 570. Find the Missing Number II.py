"""
570. Find the Missing Number II

Giving a string with number from 1-n in random order, 
but miss 1 number.Find that number.

Example
Given n = 20, str = 19201234567891011121314151618
return 17
"""
class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        from collections import defaultdict
        map = defaultdict(bool)
        return self.dfs(str, map, n, 0)

    def dfs(self, str, map, n, index):
        if index == len(str):
            result = []
            for i in xrange(1, n + 1):
                if not map[i]:
                    result.append(i)
            return result[0] if len(result) == 1 else -1
        if str[index] == '0':
            return -1
        for j in xrange(1, 3):
            num = int(str[index:index + j])
            if num >= 1 and num <= n and not map[num]:
                map[num] = True
                target = self.dfs(str, map, n, index + j)
                if target != -1:
                    return target
                map[num] = False
        return -1
