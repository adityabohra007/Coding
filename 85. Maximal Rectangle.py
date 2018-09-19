class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        result = 0
        heights = [0 for _ in xrange(n)]
        for row in matrix:
            for index, num in enumerate(row):
                heights[index] = heights[index] + 1 if num == '1' else 0
            result = max(result, self.find_max_rec(heights))
        return result

    def find_max_rec(self, heights):
        stack = []
        ret = 0
        for index, h in enumerate(heights + [-1]):
            while stack and heights[stack[-1]] >= h:
                pop_index = stack.pop()
                left = stack[-1] if stack else -1
                width = index - left - 1
                ret = max(ret, width * heights[pop_index])
            stack.append(index)
        return ret

