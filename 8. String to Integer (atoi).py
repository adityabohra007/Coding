class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        i = 0
        sign = 1
        result = 0
        maxValue = (1 << 31)-1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1

        for i in xrange(i, len(str)):
            if str[i].isdigit():
                result = result*10 + int(str[i])
                if result > maxValue:
                    break
            else:
                break

        result = result*sign
        if result > maxValue:
            return maxValue
        elif result < -maxValue:
            return -maxValue-1
        return result
