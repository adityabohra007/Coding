class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        tmp = 0
        num1 = list(num1)
        num2 = list(num2)
        result = ''
        while tmp or num1 or num2:
            num = 0
            num += tmp
            if num1:
                num += int(num1.pop())
            if num2:
                num += int(num2.pop())
            tmp = num // 10
            result = str(num % 10) + result
        return result
