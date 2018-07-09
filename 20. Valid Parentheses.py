class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = []
        for c in s:
            if c in ['(', '[', '{']:
                q.append(c)
            elif c == ')':
                if len(q) == 0 or q[-1] != '(':
                    return False
                q.pop()
            elif c == ']':
                if len(q) == 0 or q[-1] != '[':
                    return False
                q.pop()
            elif c == '}':
                if len(q) == 0 or q[-1] != '{':
                    return False
                q.pop()
        return len(q) == 0
