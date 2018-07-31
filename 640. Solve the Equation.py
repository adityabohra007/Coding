class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        equations = equation.split("=")
        lx, ln = self.cal(equations[0])
        rx, rn = self.cal(equations[1])
        if lx == rx:
            if ln == rn:
                return "Infinite solutions"
            else:
                return "No solution"
        if ln == rn:
            return "x=0"
        return "x="+str((rn-ln)//(lx-rx))

    def cal(self, s):
        x, num = 0, 0
        f = 1
        i = 0
        for j in xrange(len(s)):
            if s[j] == 'x':
                if s[i:j] == '':
                    x += f
                else:
                    x += f*int(s[i:j])
                i = j+1
            elif s[j] == '-':
                if s[i:j] != '':
                    num += f*int(s[i:j])
                f = -1
                i = j+1
            elif s[j] == '+':
                if s[i:j] != '':
                    num += f*int(s[i:j])
                f = 1
                i = j+1
            elif j == len(s)-1 and i <= j:
                num += f*int(s[i:j+1])
        return x, num
