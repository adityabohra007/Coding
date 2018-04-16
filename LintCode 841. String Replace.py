"""
暴力法，加上幾個優化：1) 遍尋時只找可能的替換字串長度, 2) 用 dict 存下替換字串的 index
time: O(s * a^2), 假設 operator "in" 的時間複雜度是 O(n)
Space: O(s) or O(a)
"""
class Solution_1:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        repLens = set()
        idxMap = {}
        for i in xrange(len(a)):
            repLens.add(len(a[i]))
            idxMap[a[i]] = i
        repLens = sorted(repLens, reverse=True)

        result = ""
        start = 0
        while start < len(s):
            found = False
            for repLen in repLens:
                end = start + repLen
                if end > len(s):
                    continue

                str = s[start: end]
                if str in a:
                    result += b[idxMap.get(str)]
                    found = True
                    start = end
                    break

            if not found:
                result += s[start]
                start += 1

        return result