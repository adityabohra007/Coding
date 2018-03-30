class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
            
            if n == number:
                break
        
        if number not in dict:
            return -1
        
        for n in dict:
            if dict[n] == 1:
                return n
        
        return -1
