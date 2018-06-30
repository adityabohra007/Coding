class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) < 1:
            return None
        q = []
        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token in ops:
                num2 = q.pop()
                num1 = q.pop()
                if token == '+':
                    q.append(num1 + num2)
                elif token == '-':
                    q.append(num1 - num2)
                elif token == '*':
                    q.append(num1 * num2)
                elif token == '/':
                    num = abs(num1) / abs(num2)
                    if num1 * num2 < 0:
                        num *= -1
                    q.append(num)
            else:
                q.append(int(token))
        return q[0]
