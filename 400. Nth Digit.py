class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = 9
        d = 2
        padding = 0

        if n >= 1 and n <= 9:
        	return n

        while True:
        	left = right + 1
        	right += 9 * (10 ** (d-1)) * (d)
        	if n >= left and n <= right:
        		padding = n - (left - 1)
        		break
        	d += 1

        num, cnt = divmod(padding, d)
        if cnt == 0:
        	return int(str((10 ** (d-1)) - 1 + num)[-1])
        else:
        	return int(str((10 ** (d-1)) + num)[cnt-1])
