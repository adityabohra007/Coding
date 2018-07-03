class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        result = 0
        q = []
        sign = 1
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1
                result += sign * num
                i -= 1
            elif c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                q.append(result)
                q.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result *= q.pop()
                result += q.pop()
            i += 1
        return result
