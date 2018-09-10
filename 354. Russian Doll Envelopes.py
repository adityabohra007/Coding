import bisect


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if envelopes is None or len(envelopes) == 0:
            return 0
        envelopes = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        heights = []
        for envelope in envelopes:
            heights.append(envelope[1])
        l = [heights[0]]
        for h in heights[1:]:
            if h > l[-1]:
                l.append(h)
            else:
                l[bisect.bisect_left(l, h)] = h
        return len(l)