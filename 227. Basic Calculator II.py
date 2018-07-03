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
        sign = '+'
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1
                if sign == '+':
                    q.append(num)
                elif sign == '-':
                    q.append(-num)
                elif sign == '*':
                    q.append(q.pop() * num)
                elif sign == '/':
                    q.append(int(q.pop() / float(num)))
                i -= 1
            elif c == '+':
                sign = '+'
            elif c == '-':
                sign = '-'
            elif c == '*':
                sign = '*'
            elif c == '/':
                sign = '/'
            i += 1
        while q:
            result += q.pop()
        return result
