class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        f = 2
        result = []

        while f * f <= num:
            while num % f == 0:
                result.append(f)
                num //= f
            f += 1

        if num > 1:
            result.append(num)

        return result
