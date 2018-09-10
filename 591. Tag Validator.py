class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and len(stack) == 0:
                return False
            if code[i: i+9] == '<![CDATA[':
                j = i+1
                i = code.find(']]>', j)
                if i < 0:
                    return False
                i += 2
            elif code[i: i+2] == '</':
                j = i+2
                i = code.find('>', j)
                if i < 0:
                    return
                tag = code[j:i]
                if len(stack) == 0 or stack[-1] != tag:
                    return False
                stack.pop()
            elif code[i: i+1] == '<':
                j = i+1
                i = code.find('>', j)
                if i < 0 or i == j or i - j > 9:
                    return False
                for k in xrange(j, i):
                    if code[k] < 'A' or code[k] > 'Z':
                        return False
                tag = code[j: i]
                stack.append(tag)
            i += 1
        return len(stack) == 0