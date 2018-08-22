class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        result, stack = 0, []
        if input is None or len(input) == 0:
            return result
        pathArr = input.split('\n')
        depth = -1
        for path in pathArr:
            name = path.replace("\t", "")
            cur_depth = path.count("\t")
            if cur_depth > depth:
                stack.append(name)
            else:
                tmp = cur_depth
                while tmp < depth:
                    stack.pop()
                    tmp += 1
                stack[-1] = name
            depth = cur_depth
            if "." in path:
                file_path = "/".join(stack)
                result = max(result, len(file_path))
        return result
