class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """

    def dropEggs(self, n):
        import math

        x = int(math.sqrt(n * 2))

        while x * (x + 1) / 2 < n:
            x += 1

        return x
