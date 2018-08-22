class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        if color is None or len(color) < 7:
            return ''
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)

        r1 = round(r*1.0/17)*17
        g1 = round(g*1.0/17)*17
        b1 = round(b*1.0/17)*17

        return '#%02x%02x%02x' % (r1, g1, b1)
