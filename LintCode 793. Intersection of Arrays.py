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
