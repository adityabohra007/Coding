"""
DFS
"""
import sys
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        if transactions is None or len(transactions) == 0:
            return 0
        self.result = sys.maxint
        hash = {}
        for transaction in transactions:
            p1 = transaction[0]
            p2 = transaction[1]
            if p1 not in hash:
                hash[p1] = -transaction[2]
            else:
                hash[p1] -= transaction[2]
            if p2 not in hash:
                hash[p2] = transaction[2]
            else:
                hash[p2] += transaction[2]
        accounts = []
        for v in hash.values():
            if v != 0:
                accounts.append(v)
        self.helper(accounts, 0, 0)
        return self.result
    
    def helper(self, accounts, start, count):
        while start < len(accounts) and accounts[start] == 0:
            start += 1
        if start == len(accounts):
            self.result = min(self.result, count)
        for i in xrange(start+1, len(accounts)):
            if accounts[start] * accounts[i] < 0:
                accounts[i] += accounts[start]
                self.helper(accounts, start+1, count+1)
                accounts[i] -= accounts[start]
        