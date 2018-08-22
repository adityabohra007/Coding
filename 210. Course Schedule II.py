class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        p = [0] * numCourses
        r = [[] for _ in xrange(numCourses)]
        for prereq in prerequisites:
            p[prereq[0]] += 1
            r[prereq[1]].append(prereq[0])
        q = []
        for i in xrange(len(p)):
            if p[i] == 0:
                q.append(i)
        result = []
        while q:
            n = q.pop(0)
            result.append(n)
            for child in r[n]:
                p[child] -= 1
                if p[child] == 0:
                    q.append(child)
        return result if len(result) == numCourses else []
