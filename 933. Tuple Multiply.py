class Solution:
    """
    @param tuple: the tuple string
    @param n: an integer
    @return: the product of all the nth element in each array
    """
    def tupleMultiply(self, tuple, n):
        # Write your code here
        if tuple is None or len(tuple) == 0:
            return 0

        tuples = tuple[1:-1].split("),(")
        result = 1
        for t in tuples:
            result = result*int(t.split(",")[n-1])
        return result
