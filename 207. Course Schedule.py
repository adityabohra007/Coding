class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        arr1 = [0 for i in xrange(numCourses)]
        arr2 = [[] for i in xrange(numCourses)]

        for prerequisite in prerequisites:
            arr1[prerequisite[0]] += 1
            arr2[prerequisite[1]].append(prerequisite[0])

        q = []
        total = 0
        for k in xrange(len(arr1)):
            if arr1[k] == 0:
                q.append(k)

        while len(q) > 0:
            course = q.pop(0)
            total += 1
            for j in arr2[course]:
                arr1[j] -= 1
                if arr1[j] == 0:
                    q.append(j)

        return total == numCourses
