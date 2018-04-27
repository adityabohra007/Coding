class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        from collections import deque

        q = deque([s])
        hash = set([s])
        min = len(s)

        while q:
            curS = q.popleft()
            for sub in dict:
                pos = curS.find(sub)
                while pos != -1:
                    newS = curS[:pos] + curS[pos + len(sub):]
                    if newS not in hash:
                        if len(newS) < min:
                            min = len(newS)
                        q.append(newS)
                        hash.add(newS)
                    pos = curS.find(sub, pos + 1)
        return min
