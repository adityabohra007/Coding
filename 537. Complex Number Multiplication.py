class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        arr1 = a.split('+')
        arr2 = b.split('+')
        arr1[0] = int(arr1[0])
        arr1[1] = int(arr1[1][:-1])
        arr2[0] = int(arr2[0])
        arr2[1] = int(arr2[1][:-1])
        result = str((arr1[0]*arr2[0])-(arr1[1]*arr2[1]))
        result += '+'
        result += str((arr1[0]*arr2[1])+(arr1[1]*arr2[0]))
        result += 'i'
        return result
