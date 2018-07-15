class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash = {}
        for c in s:
            hash[c] = hash[c] + 1 if c in hash else 1
        hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        return ''.join(map(lambda c: c[0]*c[1], hash))