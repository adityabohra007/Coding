"""
Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        map = {}
        for n in nums:
            map[n] = 1

        result = 0
        for n in nums:
            if n in map:
                len = 1
                del (map[n])
                left = n - 1
                right = n + 1
                while left in map:
                    len += 1
                    del (map[left])
                    left -= 1
                while right in map:
                    len += 1
                    del (map[right])
                    right += 1
                if len > result:
                    result = len
        return result