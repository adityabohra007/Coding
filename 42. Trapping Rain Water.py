class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        maxl, maxr, result = 0, 0, 0
        l = 0
        r = len(height) - 1

        while l < r:
            if height[l] <= height[r]:
                maxl = max(maxl, height[l])
                result += maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                result += maxr - height[r]
                r -= 1
        return result
