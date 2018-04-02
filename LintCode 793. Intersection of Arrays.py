class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):

        ret = self.helper(arrs)
        return len(ret)

    def helper(self, arrs):
        if len(arrs) == 1:
            return arrs[0]

        left = self.helper(arrs[:len(arrs) / 2])
        right = self.helper(arrs[len(arrs) / 2:])

        return list(set(left) & set(right))

"""
Solution2 没有验证
如果有一个arr里有重复的值，答案不准确
"""
class Solution2:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        #
        M = {}
        for i in arrs:
            for j in i:
                if j in M:
                    M[j] = M[j] + 1
                else:
                    M[j] = 1
        ans = 0
        for k, v in M.iteritems():
            if v == len(arrs):
                ans += 1
        return ans
