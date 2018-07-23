class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if flowerbed is None or len(flowerbed) == 0:
            return
        for i in xrange(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                next = 0 if i + 1 == len(flowerbed) else flowerbed[i+1]
                pre = 0 if i == 0 else flowerbed[i-1]
                if pre + next == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
