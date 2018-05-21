"""
Given a permutation which may contain repeated numbers, 
find its index in all the permutations of these numbers, 
which are ordered in lexicographical order. The index begins at 1.

Example

Given the permutation [1, 4, 2, 2], return 3.
"""
from collections import defaultdict


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndexII(self, A):
        result = 1
        factor = 1
        dup = 1
        map_of_nums_less_than_i = defaultdict(int)
        for i in xrange(len(A) - 1, -1, -1):
            amount_nums_less_than_i = 0
            map_of_nums_less_than_i[A[i]] += 1
            dup *= map_of_nums_less_than_i[A[i]]
            for j in xrange(i + 1, len(A)):
                if A[i] > A[j]:
                    amount_nums_less_than_i += 1
            result += factor * amount_nums_less_than_i / dup
            factor *= len(A) - i
        return result
