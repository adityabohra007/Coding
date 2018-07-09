class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = ""
        if not words or len(words) == 0:
            return result
        if len(words) == 1:
            return words[0]
        hash = {}
        num = {}
        for i in xrange(len(words)-1):
            cur = words[i]
            next = words[i+1]
            p = 0
            while p < len(cur) and p < len(next):
                if cur[p] == next[p]:
                    if cur[p] not in num:
                        num[cur[p]] = 0
                    p += 1
                else:
                    if cur[p] not in num:
                        num[cur[p]] = 0
                    if next[p] not in num:
                        num[next[p]] = 1
                    else:
                        num[next[p]] += 1
                    if cur[p] not in hash:
                        hash[cur[p]] = [next[p]]
                    else:
                        if next[p] not in hash[cur[p]]:
                            hash[cur[p]].append(next[p])
                        else:
                            num[next[p]] -= 1
                    break
            p -= 1
            for c in cur[p+1:]:
                if c not in num:
                    num[c] = 0
            for c in next[p+1:]:
                if c not in num:
                    num[c] = 0
        q = []
        for c, occurNum in num.items():
            if occurNum == 0:
                q.append(c)

        while q:
            cr = q.pop(0)
            result += cr
            if cr in hash:
                for child in list(set(hash[cr])):
                    num[child] -= 1
                    if num[child] == 0:
                        q.append(child)
        return result if len(result) == len(num) else ""
