class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0

        # top
        lo = 0
        hi = x
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if self.checkRow(mid, image):
                hi = mid
            else:
                lo = mid
        if self.checkRow(lo, image):
            top = lo
        else:
            top = hi

        # bottom
        lo = x
        hi = m-1
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if self.checkRow(mid, image):
                lo = mid
            else:
                hi = mid
        if self.checkRow(hi, image):
            bottom = hi
        else:
            bottom = lo

        # left
        lo = 0
        hi = y
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if self.checkCol(mid, image):
                hi = mid
            else:
                lo = mid
        if self.checkCol(lo, image):
            left = lo
        else:
            left = hi

        # right
        lo = y
        hi = n-1
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if self.checkCol(mid, image):
                lo = mid
            else:
                hi = mid
        if self.checkCol(hi, image):
            right = hi
        else:
            right = lo

        return (right - left + 1) * (bottom - top + 1)

    def checkRow(self, row, image):
        for i in xrange(len(image[0])):
            if image[row][i] == '1':
                return True
        return False

    def checkCol(self, col, image):
        for i in xrange(len(image)):
            if image[i][col] == '1':
                return True
        return False
