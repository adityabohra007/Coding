class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        l = [0] * 26
        for task in tasks:
            l[ord(task) - ord('A')] += 1
        l = sorted(l, reverse=True)
        for i in xrange(len(l)):
            if l[i] < l[0]:
                break
        return max(len(tasks), (l[0] - 1) * (n + 1) + i)