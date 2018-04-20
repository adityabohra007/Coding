class Solution(object):
    def minArea(self, image, x, y):
        if not image or len(image) == 0 or len(image[0]) == 0:
            return 0

        m = len(image)
        n = len(image[0])

        low = 0
        high = x
        while low + 1 < high:
            mid = (low + high) / 2
            if self.checkRow(mid, image):
                high = mid
            else:
                low = mid
        if self.checkRow(low, image):
            top = low
        else:
            top = high

        low = x
        high = m - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if self.checkRow(mid, image):
                low = mid
            else:
                high = mid
        if self.checkRow(high, image):
            bottom = high
        else:
            bottom = low

        low = 0
        high = y
        while low + 1 < high:
            mid = (low + high) / 2
            if self.checkColumn(mid, image):
                high = mid
            else:
                low = mid
        if self.checkColumn(low, image):
            left = low
        else:
            left = high

        low = y
        high = n - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if self.checkColumn(mid, image):
                low = mid
            else:
                high = mid
        if self.checkColumn(high, image):
            right = high
        else:
            right = low

        return (bottom - top + 1) * (right - left + 1)

    def checkRow(self, x, image):
        for i in xrange(len(image[0])):
            if image[x][i] == "1":
                return True
        return False

    def checkColumn(self, x, image):
        for i in xrange(len(image)):
            if image[i][x] == "1":
                return True
        return False
