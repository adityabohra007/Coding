"""
Given a string, find all permutations of it without duplicates.

Example

Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].
"""
class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        self.result = []

        arr = []
        for s in str:
            arr.append(s)
        arr = sorted(arr)
        used = [False] * len(str)
        self.dfs(arr, used, '')
        return self.result

    def dfs(self, arr, used, tmp):
        if len(tmp) == len(arr):
            self.result.append(tmp[:])
            return

        for i in xrange(len(arr)):
            if used[i] == False and (i == 0 or arr[i] != arr[i - 1]
                                     or used[i - 1] == True):
                used[i] = True
                self.dfs(arr, used, tmp + arr[i])
                used[i] = False
