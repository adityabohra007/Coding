# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):

        low = 1
        high = n

        while low + 1 < high:
            mid = (low + high) / 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid

        if isBadVersion(low):
            return low
        else:
            return high
