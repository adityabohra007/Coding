class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for str in strs:
            tran = ''.join(sorted(str))
            if tran in hash:
                hash[tran].append(str)
            else:
                hash[tran] = [str]
        result = []
        for v in hash.values():
            result.append(v)
        return result
