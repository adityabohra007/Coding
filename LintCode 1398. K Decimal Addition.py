class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        # Write your code here
        x = int(a, k)
        y = int(b, k)
        total = x + y
        result = ""
        while total > 0:
            result = str(total%k) + result
            total /= k
        return result