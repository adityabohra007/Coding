class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        num = bin(n)[2:]
        left = 0
        right = len(num)-1
        while left < right:
            if num[left] != num[right]:
                return False
            left += 1
            right -= 1
        return True
