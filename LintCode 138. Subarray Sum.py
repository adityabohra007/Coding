class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        sum = 0
        arr = []
        arr.append(sum)
        for num in nums:
            sum += num
            arr.append(sum)
        
        result = []
        for i in xrange(len(arr)-1):
            for j in xrange(i+1, len(arr)):
                if arr[j] - arr[i] == 0:
                    return [i, j-1]
            